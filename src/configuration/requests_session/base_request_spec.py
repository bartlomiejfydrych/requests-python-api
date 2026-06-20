from typing import Optional, Union

import requests


# ==========================================================================================================
# BASE REQUEST SPEC
# ==========================================================================================================

class BaseRequestSpec(requests.Session):
    """
    NOTE FOR ME:
    Odpowiednik RequestSpecification z REST Assured.

    {requests.Session} sam scala {self.params} oraz {self.headers} z parametrami/nagłówkami
    podanymi przy konkretnym wywołaniu (np. session.get(url, params={"extra": "1"})),
    dlatego wystarczy nadpisać metodę {request}, aby dokleić {base_url} do każdego żądania
    wysyłanego przez tę sesję.
    """

    def __init__(
            self,
            base_url: str,
            default_params: Optional[dict] = None,
            default_headers: Optional[dict] = None,
    ) -> None:
        super().__init__()
        self.base_url = base_url

        self.headers.update({"Content-Type": "application/json"})
        if default_headers:
            self.headers.update(default_headers)

        if default_params:
            self.params.update(default_params)

    def request(self, method, url, *args, **kwargs):
        return super().request(method, self._build_url(url), *args, **kwargs)

    def _build_url(self, url: Union[str, bytes]) -> str:
        # NOTE FOR ME: {requests.Session.request} dopuszcza {url} jako str lub bytes,
        # dlatego tutaj normalizujemy do str, zanim cokolwiek zrobimy z {url}.
        if isinstance(url, bytes):
            url = url.decode("utf-8")

        if url.startswith("http://") or url.startswith("https://"):
            return url
        return f"{self.base_url.rstrip('/')}/{url.lstrip('/')}"
