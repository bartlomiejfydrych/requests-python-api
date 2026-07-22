from dataclasses import dataclass
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode, unquote

# ==========================================================================================================
# FIELDS
# ==========================================================================================================

_SENSITIVE_KEYS = {"key", "token", "authorization"}

_MASK = "*** MASKED ***"


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# ------------------------------
# URL (ULTRA SAFE – URI PARSING)
# ------------------------------

def sanitize_url(url: str) -> str:
    if url is None or url.strip() == "":
        return url

    try:
        scheme, netloc, path, query, fragment = urlsplit(url)

        if not query:
            return url

        # NOTE FOR ME:
        # {parse_qsl(keep_blank_values=True)} = Javowe ręczne {query.split("&")} + {pair.split("=", 2)}.
        # {keep_blank_values=True} zachowuje parametry bez wartości (np. "foo="), tak jak w Javie
        # (gdzie {pair.length > 1 ? pair[1] : ""} też dopuszczało pusty string).
        params = parse_qsl(query, keep_blank_values=True)

        new_params = [
            (key, _MASK if _is_sensitive(unquote(key)) else value)
            for key, value in params
        ]

        new_query = urlencode(new_params)

        return urlunsplit((scheme, netloc, path, new_query, fragment))

    except ValueError:
        # fallback → regex (last resort)
        return _fallback_sanitize(url)


def _fallback_sanitize(url: str) -> str:
    import re

    sanitized = url
    for key in _SENSITIVE_KEYS:
        sanitized = re.sub(rf"({key}=)[^&]+", rf"\1{_MASK}", sanitized, flags=re.IGNORECASE)

    return sanitized


# -------
# HEADERS
# -------

def mask_headers(headers: dict) -> dict:
    masked: dict = {}

    if not headers:
        return masked

    for name, value in headers.items():
        masked[name] = _MASK if _is_sensitive(name) else value

    return masked


# ------------
# QUERY PARAMS
# ------------

def mask_query_params(params: dict) -> dict:
    if not params:
        return {}

    return {
        key: (_MASK if _is_sensitive(key) else value)
        for key, value in params.items()
    }


# ----------
# ALL-IN-ONE
# ----------

# NOTE FOR ME:
# W przeciwieństwie do Javy (FilterableRequestSpecification.getQueryParams()), {requests.PreparedRequest}
# nie udostępnia osobnej mapy query params - są one już częścią {request.url}. Dlatego {mask_all} maskuje
# tylko {url} (który i tak obejmie query params) oraz {headers}. {mask_query_params()} zostaje dostępne
# osobno, gdybyś kiedyś potrzebował zamaskować gotową mapę params przed zbudowaniem requestu.
def mask_all(request) -> "MaskedRequest":
    return MaskedRequest(
        url=sanitize_url(request.url),
        headers=mask_headers(dict(request.headers)),
    )


# ==========================================================================================================
# METHODS – SUB
# ==========================================================================================================

def _is_sensitive(key: str) -> bool:
    return key is not None and key.lower() in _SENSITIVE_KEYS


# ==========================================================================================================
# DTO
# ==========================================================================================================

@dataclass(kw_only=True)
class MaskedRequest:
    url: str
    headers: dict
