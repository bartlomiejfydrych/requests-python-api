# 🌐Requests i testy – notatki

# 📑Spis treści

- [START – rozpoczęcie pisania testów](#start--rozpoczęcie-pisania-testów)
  - [Dostępy](#dostępy)
  - [config.ini](#configini)
  - [.env](#env)
  - [config.py](#configpy)
  - [base_url_builder.py (opcjonalne)](#base_url_builderpy-opcjonalne)
  - [Requests Session](#requests-session)
  - [Test Base](#test-base)
  - [Pytest mark – tagi testów (opcjonalne)](#pytest-mark--tagi-testów-opcjonalne)
  - [Porównywanie obiektów – utils compare](#porównywanie-obiektów--utils-compare)
  - [Endpoints](#endpoints)
  - [Enums](#enums)
  - [Payloads](#payloads)
  - [Endpoints – pozostałe](#endpoints--pozostałe)
  - [Test – mały](#test--mały)
  - [Expected responses](#expected-responses)
  - [DTO](#dto)
  - [Utils tests](#utils-tests)
  - [Logi](#logi)
  - [Test – ostateczny](#test--ostateczny)
  - [Dokumentacja](#dokumentacja)
- [config.ini – Wymagalność podziału na sekcje](#configini--wymagalność-podziału-na-sekcje)
- [DTO → Pydantic – aliasy pól (camelCase JSON ↔ snake_case Python)](#dto--pydantic--aliasy-pól-camelcase-json--snake_case-python)

---

# 📄START – rozpoczęcie pisania testów

## Dostępy

1. Zakładamy `konta` i inne `dostępy`
    - W przypadku tego projektu zakładamy `konto` oraz zdobywamy `API key` oraz `token` na stronie **Trello**
    - Szczegóły w `README` katalogu `📂trello-configuration`

## config.ini

Wszelkie ustawienia projektu warto trzymać i odczytywać z osobnego pliku, aby nie musieć nic zmieniać w samym kodzie.  
Zapisujemy w nim takie rzeczy jak:
- bazowy URL w całości
- bazowy URL rozbity na osobne segmenty:
  - protokół
  - subdomena
  - domena
  - TLD
  - Numer

1. W głównym katalogu **projektu** dodajemy **Python Package** o nazwie `src`.

   Dlaczego `src` jako **Package**?  
   Żebyś mógł importować z niego w testach:
   ```python
   python# test_example.py
   from src.config import BASE_URL, API_KEY  # działa tylko gdy src ma __init__.py
   ```
   Bez `__init__.py` Python nie wie, że `src` to moduł i import się wysypie.
   
   `__init__.py` — co w środku?  
   Najczęściej pusty plik — jego samo istnienie wystarczy:
   ```python
   # src/__init__.py
   # (pusty)
   ```
2. W katalogu `src` dodajemy **katalog** o nazwie `resources`
3. W katalogu `resources` dodajemy **katalog** o nazwie `configuration`
4. Tworzymy w nim **plik** o nazwie `config.ini`
5. Umieszczamy w nim takie dane:
   ```ini
   # File config.ini - project variables
   
   # ALLURE REPORT
   [allure]
   allureReport=true
   
   # BASE URL
   [base_url]
   baseUrl=https://api.trello.com/1
   # If you want use string builder
   baseUrlProtocol=https
   baseUrlSubdomain=api
   baseUrlDomain=trello
   baseUrlTLD=com
   baseUrlNumber=1
   ```
   Python `.ini` — wymaga sekcji!  
   configparser w Pythonie został zaprojektowany pod format .ini, który zawsze wymaga przynajmniej jednej sekcji
   w nagłówkach [nazwa_sekcji]. To nie jest opcja — to wymóg formatu.

### ⚠️ Ważna rzecz do sprawdzenia w Twoim `config.ini`

Zwróć uwagę, że nazwy kluczy mają wielkość liter taką, jak w plikach Javy (`baseUrl`, `allureReport`) — to się zgadza
z Twoim `.ini`. Dobrze.

Natomiast `configparser` **domyślnie zamienia nazwy kluczy na małe litery** przy odczycie (nie nazwy sekcji — te są
case-sensitive, ale klucze owszem). To może być problem:To potwierdza ważną pułapkę: **`configparser` zamienia nazwy
kluczy na małe litery**, ale `has_option()` też automatycznie obniża wielkość liter przy sprawdzaniu — więc
`has_option("base_url", "baseUrl")` zwraca `True`, mimo że realnie w słowniku jest `baseurl`. Dzięki temu Twój kod
**zadziała poprawnie** — nie musisz nic zmieniać, ale warto, żebyś wiedział, że to się dzieje "pod maską", bo:

- Jeśli kiedykolwiek zechcesz iterować po wszystkich kluczach sekcji (`config["base_url"].keys()`), zobaczysz same małelitery, nie `baseUrl`
- W Javie `Properties` rozróżniał wielkość liter dokładnie tak, jak zapisano — to jedna z różnic, o której dobrze wiedzieć przy debugowaniu

Twój kod jest poprawny i gotowy do użycia z aktualnym `config.ini`.

## .env

1. Upewniamy się, że mamy dodane **dependency** o nazwie `python-dotenv`
2. W **katalogu głównym** projektu tworzymy zwykły katalog o nazwie `environment`
3. W katalogu `environment` tworzymy plik (File) o nazwie `.env.example` i definiujemy tam szablon naszych zmiennych
4. W tym samym katalogu tworzymy plik (File) o nazwie `.env`
5. W pliku `.env` do zdefiniowanego szablonu z naszymi zmiennymi dodajemy ich realne wartości

## config.py

1. W package `src` tworzymy **package** o nazwie `configuration`
2. W tym package tworzymy plik Python (Python File) o nazwie `config.py`
3. (Opcjonalne) W package `src` tworzymy package o nazwie `enums`
4. (Opcjonalne) W package `enums` tworzymy package o nazwie `configuration`
5. (Opcjonalne) W package `configuration` tworzymy plik Python (Python File) o nazwie `logs_mode.py`
6. (Opcjonalne) W tym pliku dodajemy enumy z nazwami typów naszych przyszłych loggerów oraz walidator dla poprawności ich wartości
7. W pliku `config.py` wczytujemy oba pliki konfiguracyjne i dodajemy metody pobierające dane ich zmiennych
8. W pliku `config.ini` dodajemy sekcje dla naszych zmiennych lub jedną ogólną np. `[config]` dla wszystkich zmiennych

## base_url_builder.py (opcjonalne)

1. W package `src/configuration` tworzymy plik `base_url_builder.py`
2. W pliku `base_url_builder.py` piszemy budowanie naszego URL ze zmiennych konfiguracyjnych projektu

## Requests Session

1. W package `src/configuration` tworzymy package o nazwie `requests_session`
2. W package `requests_session` tworzymy plik `base_request_spec.py`
3. Jak to działa:  
   Sercem rozwiązania jest `BaseRequestSpec` — klasa dziedzicząca po `requests.Session`. `requests.Session` ma wbudowaną
   funkcję, której Java/REST Assured nie ma za darmo: jej `params` i `headers` **automatycznie scalają się** z parametrami
   podanymi przy konkretnym wywołaniu (`session.get(url, params={"extra": "123"})`). Dorzuciłem tylko nadpisanie
   `request()`, żeby sama doklejała `base_url` — bo to jedyna rzecz, której natywnie `requests` nie robi.
4. W package `requests_session` tworzymy plik `config_request_spec.py`
5. W nim definiujemy pobierające specyfikację requestów, czyli:
   - Request, który ma mieć zawsze klucz i token
   - Request bez klucza api
   - Request bez tokenu

Przykład zastosowania tego później w teście:
```python
"""
Przykładowy test pokazujący, jak korzystać z ConfigRequestSpec.
Wymaga zmiennych środowiskowych: TRELLO_API_KEY, TRELLO_TOKEN
(opcjonalnie: TRELLO_BASE_URL).
"""
from configuration.requests_session.config_request_spec import get_request_specification


def test_get_boards():
    session = ConfigRequestSpec.get_request_specification()

    # "key" i "token" zostaną automatycznie dodane jako query params
    response = session.get("/1/members/me/boards")

    assert response.status_code == 200


def test_create_board():
    session = ConfigRequestSpec.get_request_specification()

    response = session.post(
        "/1/boards",
        params={"name": "Mój testowy board"},  # dodatkowy param tylko dla tego requestu
    )

    assert response.status_code == 200


def test_request_without_token_returns_401():
    session = ConfigRequestSpec.get_request_specification_without_token()

    response = session.get("/1/members/me/boards")

    assert response.status_code == 401
```

## Test Base

1. W package `src` tworzymy package o nazwie `tests`
2. W package `tests` tworzymy package o nazwie `base`
3. W package `base` tworzymy plik o nazwie `test_base.py`
4. W pliku `test_base.py` deklarujemy:
   - Zmienne dla sesji requestów np. by był zawsze przesyłany token i klucz
   - Zmienne/Obiekty pomocnicze jak Faker lub Random
   - `setup_class(cls)`, która wczytuje sesje dla testów
   - `teardown_class(cls)`, która zamyka sesje na koniec testów

## Pytest mark – tagi testów (opcjonalne)

1. W głównym katalogu projektu tworzymy plik o nazwie `pytest.ini`
2. W pliku `pytest.ini` definiujemy takie markery:
   ```ini
   [pytest]
   
   ; dodaje katalog src do sys.path, żeby działały importy typu
   ; "from configuration..." / "from tests.base.test_base import TestBase"
   ; bez ręcznego ustawiania PYTHONPATH (wymaga pytest >= 7.0)
   pythonpath = src
   
   ; pozwala odpalić po prostu "pytest" z roota, bez podawania ścieżki do testów
   testpaths = src/tests
   
   markers =
       flaky: testy niestabilne, które mogą czasem failować bez zmian w kodzie
       positive: scenariusze pozytywne (happy path)
       negative: scenariusze negatywne (błędne dane, brak autoryzacji, walidacje itd.)
   
   ; jeśli użyjesz markera, który nie jest zarejestrowany powyżej (np. literówka),
   ; pytest zgłosi błąd przy starcie zamiast po cichu zignorować marker
   addopts = --strict-markers
   ```
3. Następnie możemy je stosować w testach według poniższego przykładu:
   ```python
   import pytest
   
   from tests.base.test_base import TestBase
   
   
   # Marker na poziomie klasy - oznacza WSZYSTKIE testy w tej klasie jako "positive"
   @pytest.mark.positive
   class TestGetBoard(TestBase):
   
       def test_get_board_returns_200(self):
           response = self.request_specification_common.get("/boards/{id}")
           assert response.status_code == 200
   
       # Dodatkowy marker na konkretnym teście - ten jeden test jest jednocześnie
       # "positive" (z klasy) oraz "flaky"
       @pytest.mark.flaky
       def test_get_board_returns_expected_name(self):
           response = self.request_specification_common.get("/boards/{id}")
           assert response.json()["name"] == "Example Board"
   
   
   # Marker na poziomie klasy - WSZYSTKIE testy w tej klasie są "negative"
   @pytest.mark.negative
   class TestGetBoardWithoutAuthorization(TestBase):
   
       def test_get_board_without_api_key_returns_401(self):
           response = self.request_specification_without_api_key.get("/boards/{id}")
           assert response.status_code == 401
   
       def test_get_board_without_token_returns_401(self):
           response = self.request_specification_without_token.get("/boards/{id}")
           assert response.status_code == 401
   ```

### ⚠️Rozwiązany problem

Jest jednak **jeden krytyczny problem**: lokalizacja `pytest.ini`.

**Problem:** masz go w `src/resources/configuration/pytest.ini`. Pytest szuka swojego pliku konfiguracyjnego
(`pytest.ini`, `pyproject.toml`, `tox.ini`, `setup.cfg`) idąc *od katalogów testów w górę po drzewie katalogów*,
aż znajdzie jeden z tych plików. `src/resources/configuration/` nie jest katalogiem nadrzędnym wobec `src/tests/`,
więc pytest **nigdy go automatycznie nie znajdzie** – musiałbyś za każdym razem odpalać
`pytest -c src/resources/configuration/pytest.ini`, co psuje się przy CI, IDE, czy po prostu gdy ktoś zapomni o fladze.

**Rozwiązanie:** `pytest.ini` musi leżeć w korzeniu projektu (obok `environment/`, `images/`, `src/`). Jako bonus, mogę
tam dorzucić opcję `pythonpath = src` – wtedy pytest sam doda `src` do `sys.path` i nie musisz już ręcznie ustawiać
`PYTHONPATH=src`, żeby działały Twoje "gołe" importy typu `from configuration.requests_session...` czy
`from tests.base.test_base import TestBase`.

`config.ini` (Twój plik konfiguracyjny aplikacji) może spokojnie zostać tam, gdzie jest – to zwykły plik z danymi,
czytany przez Twój kod, więc jego lokalizacja nie ma znaczenia dla pytest.

Po tej zmianie, z roota projektu wystarczy odpalić po prostu `pytest` i wszystko zadziała: znajdzie testy
w `src/tests`, doda `src` do ścieżki importów i będzie pilnować literówek w markerach.

## Porównywanie obiektów – utils compare

⚠️**UWAGA!** Należy pamiętać, by mieć dodane dependency **deepdiff** (`pip install deepdiff`)

1. W package `src` tworzymy package o nazwie `utils`.  
   W nim będziemy trzymać funkcje pomocnicze dla **wszystkich** testów.
2. W package `src/utils` tworzymy plik o nazwie `utils_compare.py`
3. W pliku `utils_compare.py` definiujemy metody (kolejność od ogółu do szczegółu):
   - Porównujące obiekty (twarde asercje i miękkie)
   - Ignorujące podane pola przy porównywaniu (wszędzie i po konkretnej ścieżce)
   - Porównujące JSON'y (twarde asercje i miękkie)
   - Usuwające podane pola rekurencyjnie przy porównywaniu z kopii
4. Definiujemy też klasę o nazwie `SoftAssertions`, która będzie mogła wykonywać wiele sprawdzeń przed wywaleniem testu

## Endpoints

1. W package `src` tworzymy package o nazwie `endpoints`
2. W package `src/endpoints` tworzymy plik o nazwie `base_endpoint.py`.  
   **Wyjaśnienie:**  
   Definiujemy w nim wrappery pobierające sesje.  
   Ukrywają przed endpointami, skąd dokładnie bierze się sesja.  
   To wygodne, bo jeśli kiedyś zmienisz sposób budowania sesji, poprawiasz tylko base_endpoint.py, a nie każdy plik endpointu.
3. W package `src/ednpoints` tworzymy package o nazwie `boards` (na wzór dokumentacji API Trello).  
   **Wyjaśnienie:**  
   W zależności od formatu dokumentacji (Swagger lub to, czego używa Trello) tworzymy strukturę katalogów i klas, która
   będzie zgodna z nią np. jeśli w Swaggerze endpoint jest zgrupowany w jeden nieduży controller to wszystkie jego warianty
   (POST, PATCH/PUT, GET, DELETE) tworzymy w jednym pliku np. `boards.py` od endpointa `/boards`.  
   W sytuacji, w której controller dla tego endpointa jest duży lub tak jak w dokumentacji Trello wiele endpointów, jest
   zgrupowane w jednej ogólnej sekcji np. `Boards`, tworzymy wtedy pod każdą metodę HTTP danego endpointa osobny plik/klasę.  
   Przykłady: `POST_create_board_endpoint`, `PUT_update_board_endpoint`, `DELETE_delete_board_endpoint` itd.
4. W package `boards` tworzymy plik o nazwie `boards_base_endpoint.py`.  
   Będzie on zawierał wspólny endpoint i metody dla wszystkich plików/metod HTTP.
5. W package `boards` tworzymy plik pod nasz pierwszy endpoint o nazwie `POST_create_board_endpoint.py`.  
   **Wyjaśnienie:**  
   Z reguły konwencja nazw plików w Python zaleca pisanie wszystkiego małymi literami, ale w testach API to nie powinno
   przeszkadzać, a moim zdaniem bardziej zwiększy czytelność.
6. W nim definiujemy metody wysyłania wybranego requesta.

## Enums

1. W package `src` tworzymy package o nazwie `enums`
2. W package `src/enums` tworzymy package o nazwie `query_parameters`
3. W package `scr/enums/query_parameters` tworzymy plik `base_query_parameter.py`.  
   Będzie on zastępował powtarzanie property `{key}` w każdym enumie osobno.
4. W package `query_parameters` tworzymy package o nazwie `boards` (Jako grupa endpointów z dokumentacji API Trello)
5. W package `boards` tworzymy kolejny package o nazwie `boards` (Jako Query Parametry dotyczące tego konkretnego endpointa)
6. W package `boards/boards` tworzymy plik o nazwie `board_base_query_parameters.py`.  
   Definiujemy w nim Query Parametry, które są wspólne dla więcej niż jednej metody HTTP dla endpointa `/board`
7. Teraz w tym samym miejscu tworzymy plik o nazwie `POST_create_board_query_parameters.py`.  
   Będzie zawierał on wszystkie enumy query parametrów dla requesta POST tworzącego tablicę.

## Payloads

1. W package `src` tworzymy package o nazwie `payloads`.  
   **Wyjaśnienie:**  
   - Nie każdy endpoint będzie miał osobny plik na payload/parametry.
   - W przypadku małej ilości parametrów dane te będą podawane jako argumenty na bieżąco w testach.
2. W package `src/payloads` tworzymy plik o nazwie `base_payload.py`
   - Definiujemy tam wspólną metodę, która będzie "dokładać" parametry jeśli nie są podane jako `null`
3. W package `src/payloads` tworzymy package o nazwie `boards`
4. W package `src/payloads/boards` tworzymy plik o nazwie `POST_create_board_payload.py`
5. W pliku tym definiujemy:
   - Że jest to `dataclass`
   - Listę query parametrów
   - Metodę pomocniczą, która zamienia payload w `dict` query parametrów

## Endpoints – pozostałe

1. Do package `endpoints` dodajemy plik `GET_get_board_endpint.py`.  
   Aby sprawdzać, czy dane dodawane przez POST rzeczywiście są prawidłowe.
2. Do package `endpoints` dodajemy plik `DEL_delete_board_endpoint.py`.  
   Aby pod koniec testu usuwać zasób dodawany przez POST.

## Test – mały

1. Mając przygotowanego naszego pierwszego mini CRUD'a w package `src/tests` tworzymy package o nazwie `api_trello`
2. W nim tworzymy package o nazwie sekcji/kontrolera z dokumentacji. W tym przypadku `boards`
3. Następnie tworzymy plik `test_POST_create_board.py.py`
4. (Opcjonalne) W pliku `test_POST_create_board.py.py` piszemy najprostszy, byle jaki test-request, aby móc skopiować
   zwracany response (jeśli nie ma takiego w dokumentacji):
   ```python
   class TestPostCreateBoard(TestBase):
   
       # ==========================================================================================================
       # TESTS
       # ==========================================================================================================
   
       def test_should_create_board(self) -> None:
           # POST
           response: Response = post_create_board("Nazwa tablicy 1", None)
           print(json.dumps(response.json(), indent=4))
           assert response.status_code == 200
           board_id: str = response.json()["id"]
           # GET
           response = get_get_board(board_id)
           print(json.dumps(response.json(), indent=4))
           assert response.status_code == 200
           # DELETE
           response = delete_delete_board(board_id)
           print(json.dumps(response.json(), indent=4))
           assert response.status_code == 200
   ```

IDE podkreśla nazwę tego testu na żółto z dopiskiem:
```
Method 'test_should_create_board' may be 'static'
```

**Robimy coś z tym?**

To ostrzeżenie pojawia się, bo w tej metodzie nie korzystasz z `self` — PyCharm widzi to i sugeruje, że skoro
nie odwołujesz się do instancji, metoda mogłaby być statyczna.

**W tym przypadku warto to ostrzeżenie zignorować**, i to celowo, w przeciwieństwie np. do `put_if_not_null`, gdzie
`@staticmethod` faktycznie było poprawną poprawką. Powody:

1. **Testy pytest nie powinny być `@staticmethod`.** Nawet jeśli konkretna metoda teraz nie używa `self`, to:
   - stracisz możliwość korzystania z atrybutów klasy z `TestBase` (np. `self.request_specification_common`,
     `self.faker`, `self.random`) bez dodatkowego dopisywania `TestBase.faker` czy podobnie,
   - jeśli kiedyś dodasz fixture jako parametr instancyjny albo będziesz chciał skorzystać z sesji z `TestBase`,
     będziesz musiał to i tak odkręcić.

2. **To częsty fałszywy pozytyw PyCharm dla klas testowych.** Framework (pytest) sam decyduje, jak wywołuje metody
   testowe — zakłada zwykły "bound method" z `self`, nawet jeśli konkretny test go nie potrzebuje. Zmiana na
   `@staticmethod` nie jest błędem technicznym, ale jest niezgodna z konwencją i utrudnia rozwój testu w przyszłości.

Jeśli takie ostrzeżenie będzie się pojawiać częściej, możesz je wyciszyć dla całego katalogu z testami w PyCharm:
**Settings → Editor → Inspections → wyszukaj "may be static"** i wyłącz dla plików w `tests/`, albo dodać komentarz
`# noinspection PyMethodMayBeStatic` nad konkretną metodą, jeśli wolisz punktowo.

## Expected responses

1. W package `src` tworzymy package o nazwie `expected_responses`
2. W package tym tworzymy package zgodny z układem w dokumentacji API, w tym przypadku `boards`
3. W package tym tworzymy plik z nazwą zgodną z endpointem, dla którego będziemy trzymać w nim oczekiwane respons'y,
   w tym przypadku `POST_create_board_expected.py`
4. W pliku tym tworzymy zmienną typu `dict`, w której umieszczamy nasz oczekiwany JSON

## Utils – Response (DTO)

1. W package `src` tworzymy package o nazwie `dto`
2. W package `src/dto` tworzymy plik o nazwie `base_dto.py`  
   Plik ten służy jako miejsce, w którym ustawiamy konfiguracje walidowania naszych DTO.
3. W package `src` tworzymy package o nazwie `exceptions`  
   Czasami warto tworzyć własne wyjątki, aby lepiej wiedzieć, co się dzieje w razie błędów.
4. W package `src/exceptions` dodajemy dwa pliki-wyjątki:
   - `exception_dto_deserialization.py`
   - `exception_json_parsing.py`
5. W package `src` tworzymy package o nazwie `utils`
6. W package `src/utils` tworzymy package o nazwie `response`
7. W package `src/utils/response` tworzymy plik o nazwie `utils_response_json_parser.py`  
   Ma on służyć do czystego parsowania bez wiązania z konkretnym DTO
8. W tym samym package tworzymy plik o nazwie `utils_response_deserializer.py`  
   W tym pliku są metody walidujące i przerabiające response na DTO zarówno dla obiektu, jak i dla listy obiektów.

## DTO

1. W package `src/dto` tworzymy plik o nazwie `base_dto.py`.  
   Plik ten ma zawierać wszystkie ustawienia naszej deserializacji, czyli:
   - `extra="forbid"` – fail, jeśli pojawią się jakieś nadmiarowe pola
   - `strict=True` – wyłączenie zamiany liczb na stringi i stringów na liczby + booleany
   - `alias_generator=to_camel` – służy do tego, aby nie musieć ręcznie dla zmiennych pisać aliasów w camelCase
   - `populate_by_name=True` – pozwala tworzyć obiekt w kodzie Python PO NAZWIE POLA (snake_case), a nie tylko po aliasie (camelCase)
2. W package `src/dto` tworzymy katalog zgodny z nazwą grupy endpointów w dokumentacji np. `boards`
3. W package `src/dto/boards` jeśli zwracane odpowiedzi z naszego CRUD'a różnią się ilością parametrów, ale mają
   większość elementów wspólnych, to tworzymy plik, który będzie najpierw przechowywał te elementy wspólne np. `board_base_dto.py`
4. Wklejamy do dowolnego **agenta AI** nasz wcześniej skopiowany response oraz dopisujemy, jakie są warunki dla pól,
   jeśli takie znamy i prosimy go o przerobienie tego na DTO.  
   **Podajemy:**
   - informację, że chcemy to na DTO
   - response
   - warunki dla pól
   - wszystkie pola mają być wymagane
   - ma być wykrywany brak jakiegoś pola
   - ma być wykrywane, jeśli pojawią się jakieś nadmiarowe pola
5. Takie DTO składa się z:
   - Zmiennych, które trzymają nazwy pól JSON, aby móc zmieniać te Stringi tylko w jednym miejscu w kodzie
   - Pola klasy/obiektu/JSON z regułami walidacyjnymi
6. Jeśli response ma w sobie inne klasy/obiekty to na nie też zakładamy osobne DTO. Najlepiej w jakimś wspólnym katalogu np. `board`
7. Jeśli jakiś obiekt/klasa ma w sobie kolejny obiekt/klasę to wewnątrz tego zakładamy kolejny katalog np. `prefs`
8. Mając **bazowe DTO**, robimy teraz DTO dla respons'ów konkretnych endpointów:
   - `POST_create_board_dto`
   - `GET_get_board_dto`
   - Oraz DTO dla pod-obiektów wewnątrz nich, najlepiej zgrupowanych w nowy pod-package o nazwie `board`

Dodatkowo, jeśli przy porównywaniu responsów będziemy chcieli pomijać jakieś pola, to żeby uniknąć podawania ich jako
String (wtedy trzeba będzie ręcznie dokonywać jego aktualizacji w każdym miejscu występowania) warto je w tym DTO
zapisywać jako zmienne np. `FIELD_LIMITS: ClassVar[str] = "limits"` dzięki czemu jak je tak wywołamy
compareObjects(responsePostDto, responseGetDto, POST_CreateBoardDto.FIELD_LIMITS); to jak coś się tu zmieni,
wtedy IDE dokona tej zmiany wszędzie.

## Utils tests

1. W package `src` tworzymy package o nazwie `utils_tests`  
   Katalog ten będzie służył do zbierania metod pomocniczych dla konkretnych klas z testami.
2. W `src/utils_tests` tworzymy plik `POST_create_board_utils.py`
3. W pliku `POST_create_board_utils.py` dodajemy takie metody jak:
   - Metoda przygotowująca oczekiwany response POST:
     - Przerabia (tylko deserializacja, bez walidacji) nasz oczekiwany String z responsem na obiekt DTO
     - Zrównuje różniące się zazwyczaj pola np.:
       - expectedResponsePostDto.name = boardName;
       - expectedResponsePostDto.id = responsePostDto.id;
     - I tak przygotowany obiekt jest zwracany i gotowy do porównywania w asercji
   - Metodę do weryfikacji zgodności naszego POST z requestem GET:
     - Wysyłany jest request GET
     - Sprawdzany jest status code
     - Response jest deserializowane i walidowane na obiekt DTO
     - Porównywany jest obiekt response POST z obiektem response GET oraz pomijane są pola, których nie chcemy porównywać
   - Metodę generującą losową nazwę tablicy:
     - Dzięki nanoTime() jest mniejsza szansa na duplikację niż przy użyciu number().randomNumber()
   - Metodę generującą losowy opis (`desc`)

## Logi

Przed rozpoczęciem pełnych testów na poważnie warto zaopatrzyć się w jakieś sposoby logowania przychodzących response,
na wypadek, gdybyśmy mieli jakieś błędy w testach i zwracanych danych.

1. Instalujemy 2 dependencies:
   - `Pygments` – służy do kolorowania JSON'a przychodzącego w response
   - `colorma` – służy do kolorowania pozostałych rzeczy np. kod statusu itp.  
     Gwarantuje poprawne działanie ANSI też poza konsolą PyCharm (np. gdybyś kiedyś odpalał to ze zwykłego `cmd.exe`)
2. W package `src` tworzymy package o nazwie `loggers`
3. W package `src/loggers` tworzymy plik o nazwie `console_colors.py`.  
   Będzie on odpowiedzialny za nadawanie kolorów w konsoli.
4. W package `src/loggers` tworzymy plik o nazwie `json_color_printer.py`.  
   Będzie on odpowiedzialny za kolorowanie zwracanego JSON przez response.
5. W package `src/utils` tworzymy plik o nazwie `utils_sensitive_data_masker.py`  
   Będzie on służył do maskowania danych poufnych w query parametrach np. klucz API i token.
6. W package `src/loggers` tworzymy plik o nazwie `console_formatter.py`.  
   Będzie on łączył kolory pozostałych elementów, kolorowy JSON oraz maskowanie danych poufnych.
7. W package `src/loggers` tworzymy plik o nazwie `console_full_formatter.py`.  
   Będzie on wyświetlał wszystkie, surowe logi, bez kolorów i bez maskowania.
8. W package `src/loggers` tworzymy plik o nazwie `http_logger.py`.  
   Jest to punkt wejścia, który na podstawie `LogsMode` z `config.py` będzie decydował co wywołać.
9. W pliku `src/configuration/requests_session/base_request_spec.py` robimy import:  
   `from loggers import http_logger`
10. I dopisujemy wywoływanie metody tutaj:  
    ```python
        def request(self, method, url, *args, **kwargs):
            response = super().request(method, self._build_url(url), *args, **kwargs)
            http_logger.log(response)
            return response
    ```
11. Teraz w pliku `.evn` możemy zarządzać włączaniem/wyłączaniem logów oraz ich ustawieniami.

## Test – ostateczny

1. Otwieramy nasz pierwszy plik z testami `src/tests/api_trello/boards/test_POST_create_board.py`
2. Na cały plik/klasę deklarujemy zmienne, jakich będziemy re-używać np. ID. W tym przypadku `board_id: Optional[str] = None`
3. Piszemy fixture/metodę `def delete_board(self)` z adnotacją `@pytest.fixture(autouse=True)` (działanie niejawne dla wszystkich testów)  
   - Zawsze, po każdym teście będzie wywoływana i odpowiedzialna za sprzątanie/usuwanie zasobu (tablicy)
   - Sprawdza, czy `board_id` jest różne od `null`
   - Jeśli tak, to wysyłany jest request `DELETE` pod to `ID`
   - Sprawdzane jest, czy jego `status code = 200`
   - Na koniec możemy dla pewności dopisać, żeby zmienna `board_id` była ponownie ustawiana na `null`
4. Dodajemy pierwszy test o nazwie `def test_p1_should_create_board_whose_name_contains_special_characters_and_numbers(self) -> None:`
   - Dzięki słówku `test_` na początku nazwy **Pytest** wie, że to jest test
   - Stwierdziłem, że fajnie będzie oznaczać jakoś testy np. w przypadku mierzenia pokrycia, wiedzieć który test co pokrywa:
     - p1, p2, p3 itd. oznaczenie dla testów pozytywnych
     - n1, n2, n3 itd. oznaczenie dla testów negatywnych
5. W teście piszemy następujące rzeczy:
   - Na samej górze deklarujemy zmienne np. `losową nazwę tablicy`
   - Wysyłamy request POST wraz z parametrami/body i zapisujemy do zmiennej typu `response`
   - Sprawdzamy `status code`
   - Zapisujemy `ID` zasobu do zmiennej
   - Deserializujemy i walidujemy ten response na obiekt DTO `POST_CreateBoardDto`
   - Przygotowujemy oczekiwany response POST:
     - Importujemy go jako `String`
     - Deserializujemy do DTO `POST_CreateBoardDto`
     - Dla pól, które zawsze się różnią, przypisujemy tutaj te z response POST np. `expected_response_post_dto.id = response_post_dto.id`
   - Porównujemy oba obiekty, ale musimy pamiętać by ignorować/wykluczać pola, które się różnią lub są nadmiarowe lub brakujące
   - Wysyłamy request GET, który jako metoda pomocnicza sprawdza zgodność z responsem POST
   - Fixture/Metoda `def delete_board(self)` z adnotacją `@pytest.fixture(autouse=True)` automatycznie usuwa stworzony zasób wysyłając request **DELETE**

## Dokumentacja

1. Przygotowujemy sobie dokumentację testową dla danego requesta/ednpointa
2. W głównym katalogu **projektu** tworzymy katalog o nazwie `documentation`
3. W katalogu `documentation` tworzymy katalog o nazwie `endpoints`
4. W katalogu `documentation/endpoints` tworzymy katalog o nazwie `boards` (zgodnie ze strukturą dokumentacji API)
5. W katalogu `documentation/endpoints/boards` tworzymy plik o nazwie `POST_CreateBoard.md`
6. W przypadku słabego prowadzenia lub nawet braku głównej dokumentacji API w projekcie testerzy mogą w takich plikach prowadzić własne notatki np.:
   - Metoda – nazwa endpointu
   - Endpoint (URL)
   - Opis
   - Ważne notatki i uwagi
   - Pokrycie testami:
     - Wklejamy cały payload lub listę wszystkich możliwych parametrów, jakie możemy podać w body
     - Pod każdym parametrem tworzymy sekcję na przypadki pozytywne i negatywne
     - Rozpisujemy wszystkie możliwe przypadki, jakie możemy podać w ramach testów
     - Przed każdym z nich wpisujemy oznaczenie testu, który pokrywa dany przypadek np. `[P1] Podanie tylko tego, wymaganego parametru`
     - Dla GET'ów, na które mogą mieć wpływ różne kombinacje endpointów/danych wklejamy response
     - I tu również pod każdym parametrem rozpisujemy przypadki testowe, czyli możliwe dane, jakie mogą/powinny wpadać
   - Query params / Payload
   - Response

---

# 📄config.ini – Wymagalność podziału na sekcje

## Różnica między `.properties` a `.ini`

### Java `.properties` — płaska struktura

Plik `.properties` to po prostu lista par klucz-wartość, bez żadnego grupowania:

```properties
baseUrl=https://api.trello.com/1
baseUrlProtocol=https
allureReport=true
```

`Properties.load()` w Javie czyta to liniowo i wszystkie klucze trafiają do jednej "płaskiej" mapy. Nie ma koncepcji
sekcji — `properties.getProperty("baseUrl")` po prostu szuka klucza w całym pliku.

### Python `.ini` — wymaga sekcji

`configparser` w Pythonie został zaprojektowany pod format `.ini`, który **zawsze** wymaga przynajmniej jednej sekcji
w nagłówkach `[nazwa_sekcji]`. To nie jest opcja — to wymóg formatu:

```ini
[config]
baseUrl = https://api.trello.com/1
baseUrlProtocol = https
allureReport = true
```

Jeśli spróbujesz wczytać plik bez żadnej sekcji:

```ini
baseUrl = https://api.trello.com/1
```

`configparser` rzuci błędem `MissingSectionHeaderError` — odmówi nawet sparsowania pliku.

### Dlaczego tak jest?

`.ini` to format wywodzący się z Windows (np. pliki konfiguracyjne starych aplikacji), gdzie sekcje służyły
do grupowania powiązanych ustawień — np. `[network]`, `[display]`, `[database]`. To "wbudowana" funkcja formatu,
której `.properties` w Javie nigdy nie miało.

### Jak to wpływa na Twój kod

W moim `_get_property` masz parametr `section: str = "config"`:

```python
def _get_property(key: str, default_value: Optional[str], section: str = "config") -> str:
    ...
    if _properties.has_option(section, key):
        return _properties.get(section, key).strip()
```

To znaczy: gdy wywołujesz np. `get_base_url()`, kod szuka klucza `baseUrl` **wewnątrz sekcji `[config]`**. Jeśli Twój
`config.ini` wygląda tak:

```ini
baseUrl = https://api.trello.com/1
```

(bez nagłówka sekcji) — parser się wysypie przy samym wczytaniu pliku.

Jeśli wygląda tak:

```ini
[inna_sekcja]
baseUrl = https://api.trello.com/1
```

— plik się wczyta, ale `_properties.has_option("config", "baseUrl")` zwróci `False`, bo szukasz w sekcji `config`,
a klucz jest w `inna_sekcja`. W efekcie zawsze trafisz na wartość domyślną (lub błąd, jeśli default nie został podany).

### Co musisz zrobić

Twój `config.ini` musi zaczynać się od:

```ini
[config]
allureReport = true
baseUrl = https://api.trello.com/1
baseUrlProtocol = https
baseUrlSubdomain = api
baseUrlDomain = trello
baseUrlTLD = com
baseUrlNumber = 1
```

### Alternatywa, gdybyś nie chciał sekcji w kodzie

Gdybyś chciał zachować płaski styl bardziej zbliżony do Javy (jedna "sekcja" zawsze), możesz to ukryć w kodzie — np.
mieć stałą `_SECTION = "config"` na górze pliku, żeby nazwa sekcji nie była "magicznym stringiem" rozsianym po funkcjach.

---

# 📄DTO → Pydantic – aliasy pól (camelCase JSON ↔ snake_case Python)

## Skąd problem

- Trello API (i większość zewnętrznych API) zwraca JSON w `camelCase` (`descData`, `idOrganization`, `shortUrl`).
- Konwencja Pythona (PEP 8) wymaga `snake_case` dla nazw pól/atrybutów — trzyma się jej cały ekosystem (stdlib, Django,
  FastAPI), PyCharm też podkreśla camelCase jako naruszenie konwencji.
- W Javie/Jacksonie ten sam problem rozwiązywał `@JsonProperty(value = "...")` na polu/parametrze konstruktora
  (lub globalnie przez `@JsonNaming(...)` / `PropertyNamingStrategy` na `ObjectMapper`).

## Trzy podejścia w Pydantic

| Opcja                                       | Jak wygląda                                        | Plusy                                                                 | Minusy                                                                            |
|---------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| **Pola wprost camelCase**                   | `descData: DescDataDto`                            | zero konfiguracji                                                     | łamie PEP 8, niespójne z resztą projektu (configi, payloady są snake_case)        |
| **`Field(alias=...)` per pole**             | `desc_data: DescDataDto = Field(alias="descData")` | pełna kontrola, jawność                                               | dużo powtarzalnego kodu przy DTO z wieloma polami                                 |
| **`alias_generator` globalnie w `BaseDto`** | `alias_generator=to_camel` w `model_config`        | snake_case wszędzie, zero powtórzeń, najbliższe odpowiednikowi z Javy | trzeba pamiętać o `populate_by_name=True`; uważać na akronimy/cyfry w nazwach pól |

**Wybrana opcja: `alias_generator=to_camel`** — spójna z resztą projektu (wszędzie indziej masz snake_case).

## Jak działa `alias`

- Domyślnie `alias` (ręczny lub wygenerowany) działa **tylko przy parsowaniu danych wejściowych** (np. `model_validate(response.json())`).
- **Nie pozwala** automatycznie tworzyć obiektu ręcznie po nazwie pola Python — trzeba by wtedy podawać alias
  (`BoardBaseDto(idOrganization=...)`), co jest niezgodne z konwencją reszty kodu.

## Po co `populate_by_name=True`

- Pozwala tworzyć obiekt **obiema metodami na raz**:
  - po aliasie (camelCase) — automatycznie przy `model_validate()` z JSON-a,
  - po nazwie pola Python (snake_case) — przy ręcznej konstrukcji w kodzie testowym, np. `BoardBaseDto(id_organization=..., short_url=...)`.
- Bez tej flagi ręczne tworzenie obiektu po nazwie pola Python rzuci błąd walidacji.

## Finalna konfiguracja w `BaseDto`

```python
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class BaseDto(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        strict=True,
        alias_generator=to_camel,      # snake_case (Python) -> camelCase (JSON), generowane automatycznie
        populate_by_name=True,          # pozwala tworzyć obiekt też po nazwie pola snake_case, nie tylko po aliasie
    )
```

Efekt: `id_organization` w Pythonie ↔ `idOrganization` w JSON-ie, bez ręcznego `Field(alias=...)` przy każdym polu.

## Przykład użycia (oba tryby działają)

```python
# 1. Deserializacja z odpowiedzi API (przez wygenerowany alias)
board = BoardBaseDto.model_validate(response.json())
print(board.id_organization)  # dostęp zawsze po snake_case

# 2. Ręczne tworzenie w teście (przez populate_by_name)
board = BoardBaseDto(
    id="507f1f77bcf86cd799439011",
    name="Test Board",
    id_organization="507f191e810c19729de860ea",
    ...
)
```

## Pułapka na przyszłość

`to_camel` może dawać nieoczekiwane wyniki dla nazw pól z akronimami lub cyframi (np. `url_v2`, `id2`).  
Warto to sprawdzić przy kolejnych DTO z Trello API, jeśli takie pola się pojawią.

## Analogia do Javy (dla porównania)

| Java (Jackson)                                                                                       | Python (Pydantic)                                                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| `@JsonProperty(value = "...")` na polu                                                               | `Field(alias="...")` na polu                                                                 |
| `@JsonNaming(PropertyNamingStrategies.LowerCamelCaseStrategy.class)` na klasie/globalnie             | `alias_generator=to_camel` w `model_config`                                                  |
| Konstruktor Javy zawsze przyjmuje nazwy pól Java (adnotacje wpływają tylko na (de)serializację JSON) | `populate_by_name=True` żeby konstruktor Python też przyjmował nazwy pól Python obok aliasów |
