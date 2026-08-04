import json
from json import JSONDecodeError
from typing import Optional
from urllib.parse import urlsplit, parse_qsl

import requests

from loggers.allure_attachment import AllureAttachment
from utils.utils_sensitive_data_masker import MaskedRequest, mask_all, mask_query_params

_SEPARATOR = "=" * 106


# NOTE FOR ME:
# Javowy {AllureFormatter} loguje dodatkowo "Request path params" i "Request form params" - to sekcje,
# których {requests} strukturalnie nie ma. Path params w REST Assured to osobna mapa (podstawiana do URL-a
# dopiero "pod spodem"); w {requests.PreparedRequest} URL trafia już w pełni zbudowany - nie ma z czego
# wyciągnąć tych wartości osobno (są nierozróżnialne od reszty ścieżki). Form params to z kolei mechanizm,
# którego ten projekt w ogóle nie używa (wszystkie requesty idą jako JSON body) - {requests} miesza je
# i tak z {body} pod jednym polem {PreparedRequest.body}, więc nie da się ich bezpiecznie odróżnić od
# JSON-a. Z tych dwóch powodów obie sekcje są tu pominięte (tak samo jak w {console_formatter.py}, który
# z tych samych przyczyn loguje tylko query params/headers/cookies/body).


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

def format_attachment(response: requests.Response) -> AllureAttachment:
    request = response.request
    masked = mask_all(request)

    method = request.method
    status_code = response.status_code
    is_error = status_code >= 400

    title = _build_title(method, status_code, is_error, masked.url)
    content = _build_content(request, response, masked)

    return AllureAttachment(title=title, content=content)


# ==========================================================================================================
# TITLE
# ==========================================================================================================

def _build_title(method: str, status_code: int, is_error: bool, url: str) -> str:
    endpoint = _extract_endpoint(url)
    icon = "❌" if is_error else "✅"

    return f"{icon} Response – {status_code} | {method} | {endpoint}"


def _extract_endpoint(url: str) -> str:
    try:
        path = urlsplit(url).path

        if not path or not path.strip():
            return "/"

        parts = path.split("/")

        if len(parts) > 2:
            return f".../{parts[2]}/..."

        return path

    except ValueError:
        return "[unknown-endpoint]"


# ==========================================================================================================
# CONTENT
# ==========================================================================================================

def _build_content(
        request: requests.PreparedRequest,
        response: requests.Response,
        masked: MaskedRequest,
) -> str:
    time_ms = round(response.elapsed.total_seconds() * 1000)
    response_size = len(response.content) if response.content is not None else 0

    query_params = mask_query_params(_extract_query_params(request.url))
    response_headers = dict(response.headers) if response.headers is not None else {}

    lines = [
        _SEPARATOR,
        "HTTP CALL",
        _SEPARATOR,
        "",
        f"STATUS: {response.status_code} {response.reason}",
        f"{request.method} – {masked.url}",
        f"TIME: {time_ms} ms",
        f"SIZE: {_format_size(response_size)}",
        "",
        _SEPARATOR,
        "REQUEST DATA",
        _SEPARATOR,
        "",
        "---------------",
        "Request headers",
        "---------------",
        "",
        _format_headers(masked.headers),
        "",
        "------------------------",
        "Request query parameters",
        "------------------------",
        "",
        _format_query_params(query_params),
        "",
        "------------",
        "Request body",
        "------------",
        "",
        _format_body(_get_request_body(request)),
        "",
        _SEPARATOR,
        "RESPONSE DATA",
        _SEPARATOR,
        "",
        "-------------",
        "Response body",
        "-------------",
        "",
        _format_body(response.text),
        "",
        "----------------",
        "Response headers",
        "----------------",
        "",
        _format_headers(response_headers),
    ]

    return "\n".join(lines)


# ==========================================================================================================
# HELPERS
# ==========================================================================================================

def _format_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} B"

    return f"{size_bytes / 1024:.2f} KB"


def _format_body(body: Optional[str]) -> str:
    if not body or not body.strip():
        return "[EMPTY BODY]"

    try:
        parsed = json.loads(body)
        return json.dumps(parsed, ensure_ascii=False, indent=2)

    except JSONDecodeError:
        return body


def _get_request_body(request: requests.PreparedRequest) -> Optional[str]:
    body = request.body

    if body is None:
        return None

    if isinstance(body, bytes):
        return body.decode("utf-8")

    return body


def _extract_query_params(url: str) -> dict:
    return dict(parse_qsl(urlsplit(url).query, keep_blank_values=True))


def _format_headers(headers: dict) -> str:
    try:
        if not headers:
            return "[NO HEADERS]"

        return json.dumps(headers, ensure_ascii=False, indent=2)

    except (TypeError, ValueError):
        return "[FAILED TO FORMAT HEADERS]"


def _format_query_params(query_params: dict) -> str:
    try:
        if not query_params:
            return "[NO QUERY PARAMETERS]"

        return json.dumps(query_params, ensure_ascii=False, indent=2)

    except (TypeError, ValueError):
        return "[FAILED TO FORMAT QUERY PARAMETERS]"
