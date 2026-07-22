from datetime import datetime
from typing import Optional
from urllib.parse import urlsplit, parse_qsl

import requests

from loggers import console_colors
from loggers.json_color_printer import print_json, print_pretty
from utils.utils_sensitive_data_masker import mask_headers, mask_query_params, sanitize_url

_MAX_BODY_LENGTH = 200


# NOTE FOR ME:
# Javowy {ConsoleFormatter} nie jest klasą statyczną (nie ma tam {static} przy metodach), ale nie ma też
# żadnych pól instancyjnych - w praktyce zachowuje się identycznie jak klasa statyczna. Dlatego, zgodnie
# z konwencją "static class -> module-level functions" stosowaną w całym projekcie, port też jest modułem
# z funkcjami, a nie klasą z pustym {__init__}.


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

def log_full(
        response: requests.Response,
        log_optional: bool,
        color_enabled: bool,
) -> None:
    request = response.request

    print(
        "\n=============================================================================================================")
    print("NEW REQUEST!")
    print(
        "=============================================================================================================")

    if log_optional:
        _log_optional(request, color_enabled)

    print("\n-----------------")
    print("BASIC INFORMATION")
    print("-----------------\n")

    # REQUEST META
    print(f"Method: {request.method}")
    print(f"URL:    {sanitize_url(request.url)}")

    # RESPONSE META
    console_colors.green(
        f"Status: {response.status_code} {response.reason}",
        color_enabled,
    )

    # NOTE FOR ME: {response.elapsed} to {datetime.timedelta} liczony automatycznie przez {requests}
    # - odpowiednik ręcznie mierzonego {elapsedTimeMs} w Javie (tam liczony ręcznie w {UnifiedLoggingFilter}
    # przez {System.currentTimeMillis()}, bo REST Assured tego nie liczy za nas).
    elapsed_ms = round(response.elapsed.total_seconds() * 1000)
    print(f"Time:   {elapsed_ms} ms")

    size = len(response.content) if response.content is not None else 0
    print(f"Size:   {size} bytes")

    # BODIES
    _log_request_body(request, color_enabled)
    _log_response_body(response.text, color_enabled)


def log_short(response: requests.Response) -> None:
    request = response.request

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nTIMESTAMP: {timestamp}")

    print(f"METHOD: {request.method}")
    print(f"URL: {sanitize_url(request.url)}")
    print(f"STATUS CODE: {response.status_code}")

    body: Optional[str] = response.text

    if body is not None and len(body) > _MAX_BODY_LENGTH:
        body = body[:_MAX_BODY_LENGTH] + "..."

    print(f"RESPONSE BODY:\n{body if body is not None else '[EMPTY BODY]'}\n")


# ==========================================================================================================
# METHODS – SUB
# ==========================================================================================================

def _log_optional(request: requests.PreparedRequest, color_enabled: bool) -> None:
    console_colors.purple("\n-----------------------------", color_enabled)
    console_colors.purple("OPTIONAL REQUEST DATA – IS ON", color_enabled)
    console_colors.purple("-----------------------------", color_enabled)

    # NOTE FOR ME:
    # {requests.PreparedRequest} nie ma osobnej mapy query params (w przeciwieństwie do Javy) - są one
    # już częścią {request.url}, więc wyciągamy je z URL-a tylko na potrzeby tego wydruku.
    query_params = dict(parse_qsl(urlsplit(request.url).query, keep_blank_values=True))

    _print_pretty("Query params", mask_query_params(query_params), color_enabled)
    _print_pretty("Headers", mask_headers(dict(request.headers)), color_enabled)
    _print_pretty("Cookies", _get_cookies(request), color_enabled)


def _log_request_body(request: requests.PreparedRequest, color_enabled: bool) -> None:
    body = request.body
    if body is None:
        return

    if isinstance(body, bytes):
        body = body.decode("utf-8")

    print("\n------------")
    console_colors.cyan("REQUEST BODY", color_enabled)
    print("------------\n")

    print_json(body, color_enabled)


def _log_response_body(response_body: Optional[str], color_enabled: bool) -> None:
    print("\n-------------")
    print("RESPONSE BODY")
    print("-------------\n")

    if response_body:
        print_json(response_body, color_enabled)
    else:
        print("[EMPTY BODY]")


def _print_pretty(title: str, data: dict, color_enabled: bool) -> None:
    if not data:
        return

    console_colors.purple(f"\n{title}:", color_enabled)

    # NOTE FOR ME:
    # Java robi to dwuetapowo (obiekt -> JSON string przez Jackson, potem string -> kolorowanie),
    # ale u nas {data} to już gotowy, pewny {dict} - nie ma potrzeby serializować go do stringa
    # tylko po to, żeby {print_json} zaraz sparsował go z powrotem. {print_pretty} pomija ten
    # zbędny roundtrip, bez utraty żadnej funkcjonalności (formatowanie i kolory bez zmian).
    print_pretty(data, color_enabled)


def _get_cookies(request: requests.PreparedRequest) -> dict:
    # NOTE FOR ME:
    # {requests} nie trzyma ciasteczek requestu jako osobnej mapy tak jak REST Assured
    # ({FilterableRequestSpecification.getCookies()}) - są one zaszyte w nagłówku {Cookie}.
    # Dlatego ręcznie parsujemy ten nagłówek na słownik.
    cookie_header = request.headers.get("Cookie")
    if not cookie_header:
        return {}

    cookies: dict = {}
    for part in cookie_header.split(";"):
        if "=" in part:
            key, value = part.strip().split("=", 1)
            cookies[key] = value

    return cookies
