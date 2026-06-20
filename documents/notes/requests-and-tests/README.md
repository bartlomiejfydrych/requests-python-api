# 🌐Requests i testy – notatki

# 📑Spis treści

- [START – rozpoczęcie pisania testów](#start--rozpoczęcie-pisania-testów)
  - [Dostępy](#dostępy)
  - [config.ini](#configini)
  - [.env](#env)
  - [config.py](#configpy)
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
