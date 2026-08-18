from typing import Optional

from providers.provider_random import faker as provider_faker
from providers.provider_random import random as provider_random

from configuration.requests_session.base_request_spec import BaseRequestSpec
from configuration.requests_session.config_request_spec import (
    get_request_specification,
    get_request_specification_without_api_key,
    get_request_specification_without_token,
)


class TestBase:
    # ==========================================================================================================
    # FIELDS
    # ==========================================================================================================

    # --------
    # REQUESTS
    # --------

    request_specification_common: Optional[
        BaseRequestSpec] = None  # Sesja ze wszystkimi parametrami (key + token) - scenariusze pozytywne
    request_specification_without_api_key: Optional[
        BaseRequestSpec] = None  # Sesja bez api key — scenariusze negatywne (np. brak autoryzacji)
    request_specification_without_token: Optional[BaseRequestSpec] = None  # Sesja bez tokena — scenariusze negatywne

    # -------
    # HELPERS
    # -------

    # NOTE FOR ME: Wywołanie *funkcji* z providera przy tworzeniu klasy (a nie samo przypisanie funkcji) —
    # zwracają one te same, zseedowane singletony co reszta frameworka (spójność z UtilsRandom itd.).
    faker = provider_faker()  # Obiekt Faker do generowania losowych danych testowych (zseedowany)
    random = provider_random()  # Obiekt Random używany do wybierania losowego elementu (zseedowany)

    # ==========================================================================================================
    # SET UP
    # ==========================================================================================================

    @classmethod
    def setup_class(cls) -> None:
        # CONFIGURATION – REQUEST
        cls.request_specification_common = get_request_specification()
        cls.request_specification_without_api_key = get_request_specification_without_api_key()
        cls.request_specification_without_token = get_request_specification_without_token()

    # ==========================================================================================================
    # TEAR DOWN
    # ==========================================================================================================

    @classmethod
    def teardown_class(cls) -> None:
        for session in (
                cls.request_specification_common,
                cls.request_specification_without_api_key,
                cls.request_specification_without_token,
        ):
            if session is not None:
                session.close()
