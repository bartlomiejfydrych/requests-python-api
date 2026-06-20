# 🌐Requests i testy – notatki

# 📑Spis treści

- [START – rozpoczęcie pisania testów](#start--rozpoczęcie-pisania-testów)
  - [Dostępy](#dostępy)
  - [config.ini](#configini)
  - [.env](#env)
  - [config.py](#configpy)
  - [base_url_builder.py (opcjonalne)](#base_url_builderpy-opcjonalne)
  - [Requests Session](#requests-session)
- [config.ini – Wymagalność podziału na sekcje](#configini--wymagalność-podziału-na-sekcje)

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
