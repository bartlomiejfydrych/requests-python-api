import random as random_module

import requests
from faker import Faker

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

    request_specification_common: requests.Session = None    # Sesja ze wszystkimi parametrami (key + token) - scenariusze pozytywne
    request_specification_without_api_key: requests.Session = None    # Sesja bez api key — scenariusze negatywne (np. brak autoryzacji)
    request_specification_without_token: requests.Session = None    # Sesja bez tokena — scenariusze negatywne

    # -------
    # HELPERS
    # -------

    faker = Faker()    # Obiekt Faker do generowania losowych danych testowych
    random = random_module.Random()    # Obiekt Random używany do wybierania losowego elementu

    # ==========================================================================================================
    # SET UP
    # ==========================================================================================================

    @classmethod
    def setup_class(cls):
        # CONFIGURATION – REQUEST
        cls.request_specification_common = get_request_specification()
        cls.request_specification_without_api_key = get_request_specification_without_api_key()
        cls.request_specification_without_token = get_request_specification_without_token()

    # ==========================================================================================================
    # TEAR DOWN
    # ==========================================================================================================

    @classmethod
    def teardown_class(cls):
        for session in (
                cls.request_specification_common,
                cls.request_specification_without_api_key,
                cls.request_specification_without_token,
        ):
            if session is not None:
                session.close()
