import requests

from loggers.json_color_printer import print_json, print_pretty


# ==========================================================================================================
# NOTE FOR ME:
# W Javie tryb FULL nie korzystał z własnego kodu (Twój UnifiedLoggingFilter świadomie nic nie robił dla
# FULL/OFF) - logowanie zapewniały natywne filtry REST Assured (RequestLoggingFilter, ResponseLoggingFilter).
# {requests} nie ma wbudowanego odpowiednika, więc ten plik jest namiastką tamtych natywnych filtrów:
# pokazuje WSZYSTKO, co {requests} udostępnia (surowe, bez maskowania danych wrażliwych - tak jak natywne
# filtry REST Assured też nic nie maskują), z ładnie sformatowanym JSON-em, ale bez kolorów.
# ==========================================================================================================


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

def log_full(response: requests.Response) -> None:
    request = response.request

    print(
        "\n=============================================================================================================")
    print("NEW REQUEST! (FULL MODE)")
    print(
        "=============================================================================================================")

    _log_request(request)
    _log_response(response)


# ==========================================================================================================
# METHODS – SUB
# ==========================================================================================================

def _log_request(request: requests.PreparedRequest) -> None:
    print("\n-------")
    print("REQUEST")
    print("-------\n")

    print(f"Method: {request.method}")
    print(f"URL:    {request.url}")

    print("\nHeaders:")
    print_pretty(dict(request.headers), False)

    body = request.body
    if body is not None:
        if isinstance(body, bytes):
            body = body.decode("utf-8")

        print("\nBody:")
        print_json(body, False)
    else:
        print("\nBody: [EMPTY BODY]")


def _log_response(response: requests.Response) -> None:
    print("\n--------")
    print("RESPONSE")
    print("--------\n")

    print(f"Status: {response.status_code} {response.reason}")

    elapsed_ms = round(response.elapsed.total_seconds() * 1000)
    print(f"Time:   {elapsed_ms} ms")

    size = len(response.content) if response.content is not None else 0
    print(f"Size:   {size} bytes")

    print("\nHeaders:")
    print_pretty(dict(response.headers), False)

    print("\nBody:")
    if response.text:
        print_json(response.text, False)
    else:
        print("[EMPTY BODY]")
