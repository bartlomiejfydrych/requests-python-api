# 🛠️Konfiguracja projektu – notatki

# 📑Spis treści

1. [🔧Konfiguracja](#konfiguracja)
   - [Python – Instalacja](#python--instalacja)
   - [IDE PyCharm  – Instalacja](#ide-pycharm--instalacja)
   - [GitHub – Tworzenie i klonowanie repozytorium](#github--tworzenie-i-klonowanie-repozytorium)
   - [Dependencies – Instalacja](#dependencies--instalacja)
   - [Dalsze kroki — rozpoczęcie pisania testów](#dalsze-kroki--rozpoczęcie-pisania-testów)
2. [🧩Dodatkowe](#dodatkowe)
   - [Typo — Poprawienie błędów w tekście dla plików (głównie Markdown) pisanych w języku polskim](#typo--poprawienie-błędów-w-tekście-dla-plików-głównie-markdown-pisanych-w-języku-polskim)
   - [Markdown — wyłączenie podkreślania błędów we fragmentach kodu](#markdown--wyłączenie-podkreślania-błędów-we-fragmentach-kodu)
3. [🔌Pluginy do IDE](#pluginy-do-ide)
   - [Rainbow Brackets](#rainbow-brackets)
   - [Allure Report](#allure-report)
4. [📚Dependencies — Opis](#dependencies--opis)
   - [pytest](#pytest)
   - [requests](#requests)
   - [pydantic](#pydantic)
   - [Faker](#faker)
   - [assertpy](#assertpy)
   - [python-dotenv](#python-dotenv)
   - [deepdiff](#deepdiff)
   - [Pygments](#pygments)
   - [colorama](#colorama)
   - [allure-pytest](#allure-pytest)

---

# 🔧Konfiguracja

## Python – Instalacja

1. Wchodzimy na stronę: https://www.python.org/
2. Klikamy `Downloads`
3. Klikamy `Download Python install manager`
4. Po uruchomieniu programu w konsoli na wszystko najlepiej wpisać `y`

## IDE PyCharm  – Instalacja

1. Wchodzimy na stronę: https://www.jetbrains.com/pycharm/
2. Klikamy `Download`
3. Klikamy `Download`
4. Instalujemy, klikając `Dalej`, `Dalej`…
5. Zaznaczamy dodatkowe opcje:
    - `Create Desktop Shortcut`
    - `Update PATH Variable (restart needed)`
    - Create Associations: `.py`

## GitHub – Tworzenie i klonowanie repozytorium

1. Wchodzimy na **GitHub** i dodajemy **nowe repozytorium**:
    - Nazwa
    - Opis
    - Szablon `.gitignore` → Język: Python
    - README.md
2. Kopiujemy **URL** naszego repozytorium
3. Wracamy do IDE i klikamy **klonowanie repozytorium**
4. Tworzymy **pusty katalog** z nazwą repozytorium i do niego **klonujemy**
5. W pliku `.gitignore` odkomentować linię z `.idea`
6. Możemy zaczynać pracę od uzupełnienia naszego `README.md`

## Dependencies – Instalacja

1. Zanim zainstalujemy cokolwiek, warto stworzyć **virtual environment** — izoluje zależności projektu od reszty systemu:
   - Otwieramy konsolę w katalogu z projektem
   - Używamy polecenia:
     ```bash
     python -m venv venv
     ```
   - Powinien po tym zostać utworzony w naszym projekcie katalog `venv`
   - Zgodnie z templatką `.gitignore` dla języka Python powinien on być **ignorowany**
2. Aktywujemy w PyCharm interpreter folderu `venv`:
   - `Hamburger menu` → `Settings...` → `Python` → `Interpreter`
   - Klikamy `Add Interpreter` → `Add Local Interpreter`
   - Zaznaczamy radiobutton `Select Existent`
   - I wybieramy ten, który używa w ścieżce `...\venv\Scripts\...`
3. Ustawiamy by w PyCharm uruchamiał się prawidłowy terminal, w prawidłowej lokalizacji projektu, z prawidłowymi ustawieniami
   i bez błędów:
   - `Hamburger menu` → `Settings...` → `Tools` → `Terminal`
   - `Project Settings` → `Start directory:` *<Tu powinna być ścieżka do naszego projektu>*
   - `Application Settings` → `Shell path:` → Wybieramy z listy: `C:\WINDOWS\system32\cmd.exe`  
     Dlaczego CMD, a nie PowerShell? Bo nie mogłem w nim ustawić ścieżki projektu oraz domyślnie blokuje wiele skryptów.  
     A CMD jest bardziej "otwarte" i po prostu działa.
   - Jeżeli po otwarciu terminalu w PyCharm widzimy coś takiego bez błędów, to znaczy, że jest okej:  
     ```bash
     Microsoft Windows [Version 10.0.26200.8457]
     (c) Microsoft Corporation. Wszelkie prawa zastrzeżone.
     
     (venv) D:\[1]-Projekty\requests-python-api>
     ```
4. Otwieramy prawidłowo już ustawiony **Terminal** w naszym projekcie w PyCharm
5. Instalujemy następujące **dependencies**:
   - **pytest** – Framework do zarządzania testami (`pip install pytest`)
   - **requests** – Budowanie i wysyłanie requestów do API (`pip install requests`)
   - **pydantic** – Mapowanie response'a na DTO (`pip install pydantic`)
   - **Faker** – Generator danych testowych (`pip install Faker`)
   - **python-dotenv** – Odczytywanie danych z pliku `.env` (`pip install python-dotenv`)
   - **deepdiff** – Rekurencyjne porównywanie danych (`pip install deepdiff`)
   - **Pygments** – Kolorowanie JSON przychodzącego w response (`pip install Pygments`)
   - **colorama** – Kolorowanie pozostałych rzeczy w konsoli również poza konsolą PyCharm np. w `cmd.exe` (`pip install colorama`)
   - **allure-pytest** – Generowanie raportów z testów (`pip install allure-pytest`)
   - Można też zainstalować wszystko naraz jednym poleceniem:
     ```bash
     pip install pytest requests pydantic Faker assertpy python-dotenv deepdiff Pygments colorama
     ```
6. Po instalacji generujemy plik z zaleznościami (To taki odpowiednik `pom.xml` z Javy):
   ```bash
   pip freeze > requirements.txt
   ```
   Dzięki temu ktoś inny (lub CI/CD) instaluje wszystko jedną komendą:
   ```bash
   pip install -r requirements.txt
   ```
7. Dodajemy do Git plik `requirements.txt` i pushujemy
8. Możemy **rozpocząć pisanie testów**

## Dalsze kroki — rozpoczęcie pisania testów

Dalsze kroki opisujące jak rozpocząć pisanie testów znajdują się w:  
📁requests-python-api (główny katalog projektu)  
&emsp;📁documents  
&emsp;&emsp;📁notes  
&emsp;&emsp;&emsp;📂requests-and-tests

---

# 🧩Dodatkowe

## Typo — Poprawienie błędów w tekście dla plików (głównie Markdown) pisanych w języku polskim

1. Klikamy `Hamburger Menu` w lewym, górnym rogu
2. Klikamy `File`
3. Klikamy `Settings`
4. Rozwijamy `Editor`
5. Klikamy `Natural Languages`
6. Klikamy `+`
7. Szukamy na liście `Polski`
8. Klikamy `Apply`
9. Klikamy `OK`

## Markdown — wyłączenie podkreślania błędów we fragmentach kodu

1. Dodajemy blok kodu z błędem np. `print("czesć World")`
2. Najeżdżamy kursorem na podkreślone słowo `czesć`
3. Po najechaniu powinno pojawić się okno z propozycją poprawy
4. Klikamy `More actions...`
5. Klikamy `Hide problems in code fences`  
   Po najechaniu na tę opcję widzimy podpowiedź, że dotyczy to tylko **Markdown**
6. Gdybyśmy chcieli to cofnąć to komunikat podpowie nam takie coś:  
   `Problem highlighting for fenced code blocks in Markdown is disabled. You can enable it in the settings under Languages and Frameworks | Markdown.`
7. Może być tak, że Git będzie chciał dodać i pushnąć plik `markdown.xml`. Dodajemy i pushujemy

---

# 🔌Pluginy do IDE

## Rainbow Brackets

### 🌈 Rainbow Brackets – Wtyczka do podświetlania nawiasów w IDE JetBrains

**Rainbow Brackets** to wtyczka do **IntelliJ IDEA**, **PyCharm**, **WebStorm**, **Android Studio** i innych IDE
z rodziny **JetBrains**, która podświetla nawiasy w różnych kolorach, ułatwiając analizę kodu.

### 📌 Kluczowe funkcje wtyczki Rainbow Brackets
✅ **Kolorowe podświetlanie nawiasów** – różne poziomy zagnieżdżenia otrzymują różne kolory.  
✅ **Obsługa wielu języków programowania** – działa m.in. w **Java, Python, JavaScript, Kotlin, HTML, XML, JSON** i wielu innych.  
✅ **Łatwa identyfikacja błędów** – pomaga znaleźć brakujące lub źle zamknięte nawiasy.  
✅ **Dostosowywanie kolorów** – użytkownik może zmieniać schemat kolorów według własnych preferencji.  
✅ **Wsparcie dla ciemnych i jasnych motywów**.  
✅ **Współpraca z innymi wtyczkami** – działa z **Material Theme UI, Atom Material Icons**, itp.

### 📦 Instalacja
1️⃣ **Otwórz:** `File → Settings → Plugins` (lub `Ctrl + Alt + S`).  
2️⃣ **Wyszukaj:** "Rainbow Brackets" w zakładce **Marketplace**.  
3️⃣ **Kliknij:** **Install**, a następnie **Restart IDE**.

### 🎨 Przykład działania i dostosowanie kolorów

Przed instalacją:
```java
public void exampleMethod() {
    if (condition) {
        while (true) {
            doSomething();
        }
    }
}
```

Po instalacji **Rainbow Brackets**:
- `{ }`, `[ ]`, `( )` będą miały różne kolory, zależnie od poziomu zagnieżdżenia.

Możesz edytować kolory w **File → Settings → Editor → Color Scheme → Rainbow Brackets**.

### 🎯 Dlaczego warto używać Rainbow Brackets?
🔹 Zwiększa **czytelność kodu** w dużych projektach.  
🔹 Pomaga znaleźć **brakujące lub nadmiarowe nawiasy**.  
🔹 Przyspiesza **debugowanie** i **analizę kodu**.  
🔹 Jest **prosta w użyciu** i nie wpływa na wydajność IDE.

## Allure Report

### 📊 Allure Report – Wtyczka

**Allure Report** to **zaawansowane narzędzie do generowania raportów testowych**. Wtyczka **Allure Plugin** dla
IDE JetBrains integruje Allure z IDE, umożliwiając szybkie generowanie, przeglądanie i analizowanie raportów
bez wychodzenia z IDE.

### 📌 Co robi wtyczka Allure Report?
✅ **Integruje raporty Allure z IDE** – pozwala otwierać i analizować wyniki testów bez wychodzenia z IDE.  
✅ **Dodaje nową zakładkę "Allure"**, w której można wizualizować raporty w graficznej formie.  
✅ **Automatycznie wykrywa katalog `allure-results`** i generuje raport jednym kliknięciem.  
✅ **Obsługuje TestNG, JUnit 4/5, Cucumber i inne frameworki** testowe.  
✅ **Pozwala przeglądać szczegóły testów** – błędy, logi, załączniki (np. screenshoty).

### 🔧 Jak zainstalować wtyczkę?
1️⃣ Otwórz **IDE** i przejdź do:
- `File → Settings → Plugins` (Windows/Linux)
- `IDE → Preferences → Plugins` (Mac)  
  2️⃣ Wyszukaj: **"Allure Report"** w zakładce **Marketplace**.  
  3️⃣ Kliknij **Install**, a potem **Restart IDE**.

### 📂 Jak używać wtyczki?
1️⃣ **Uruchom testy**, które zapisują wyniki do `allure-results`.  
2️⃣ W **dolnym panelu IDE** przejdź do zakładki **"Allure"**.  
3️⃣ Kliknij **"Generate Report"**, aby zobaczyć wyniki w IDE.  
4️⃣ Możesz nawigować po testach, sprawdzać błędy i załączniki.

### **📢 Zalety wtyczki Allure Report**
🚀 **Nie trzeba otwierać raportów w przeglądarce** – wszystko działa w IDE.  
🔍 **Szybki podgląd wyników testów** bez dodatkowych poleceń w terminalu.  
📊 **Wizualizacja błędów, logów i statystyk** testów.  
🛠️ **Łatwa integracja z popularnymi frameworkami** testowymi.

Jeśli pracujesz z Allure, ta wtyczka **znacznie ułatwia życie**! 🔥

---

# 📚Dependencies — Opis

## 📕pytest

**pytest** to popularny framework do testowania w Pythonie, używany zarówno do prostych testów jednostkowych, jak i bardziej rozbudowanych testów integracyjnych, API czy end-to-end.

Można go traktować jako narzędzie, które:

* wykrywa i uruchamia testy,
* raportuje wyniki,
* udostępnia mechanizmy przygotowywania danych testowych,
* pozwala rozszerzać funkcjonalność za pomocą wtyczek.

Pytest jest rozwijany przez społeczność skupioną wokół pytest.

### Najważniejsze cechy

#### 1. Prosta składnia

Testy są zwykłymi funkcjami Pythona:

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

Uruchomienie:

```bash
pytest
```

Pytest automatycznie znajdzie funkcje zaczynające się od `test_`.

#### 2. Rozbudowane asercje

Nie trzeba używać specjalnych metod typu `assertEquals()`.

Wystarczy zwykły `assert`:

```python
def test_user_name():
    assert user.name == "Jan"
```

Jeśli test nie przejdzie, pytest pokaże szczegółowe informacje o porównywanych wartościach.

Przykład błędu:

```python
assert "Adam" == "Jan"
```

Raport wskaże dokładnie różnicę między wartościami.

#### 3. Fixtures

Fixtures służą do przygotowywania danych lub środowiska testowego.

```python
import pytest

@pytest.fixture
def user():
    return {"name": "Jan"}

def test_user(user):
    assert user["name"] == "Jan"
```

Typowe zastosowania:

* tworzenie obiektów testowych,
* połączenia z bazą danych,
* uruchamianie serwisów testowych,
* przygotowanie plików tymczasowych.

#### 4. Parametryzacja testów

Pozwala uruchomić ten sam test dla wielu zestawów danych.

```python
import pytest

@pytest.mark.parametrize(
    "a,b,result",
    [
        (1, 2, 3),
        (5, 5, 10),
        (10, 0, 10)
    ]
)
def test_add(a, b, result):
    assert a + b == result
```

Pytest wykona trzy niezależne przypadki testowe.

#### 5. Bogaty ekosystem wtyczek

Popularne rozszerzenia:

* pytest-xdist – uruchamianie testów równolegle,
* pytest-cov – integracja z raportami pokrycia kodu,
* pytest-mock – łatwiejsze mockowanie,
* pytest-html – raporty HTML,
* pytest-bdd – podejście BDD (Given/When/Then).

### Struktura projektu

Przykład:

```text
project/
│
├── src/
│   └── calculator.py
│
└── tests/
    └── test_calculator.py
```

Pliki testowe zwykle:

* zaczynają się od `test_`,
* lub kończą na `_test.py`.

### Uruchamianie

Wszystkie testy:

```bash
pytest
```

Konkretny plik:

```bash
pytest tests/test_api.py
```

Konkretna funkcja:

```bash
pytest tests/test_api.py::test_login
```

Więcej szczegółów:

```bash
pytest -v
```

### Najczęstsze zastosowania w QA

Jako tester możesz spotkać pytest przy:

* testach API (np. z biblioteką `requests`),
* automatyzacji regresji,
* testach integracyjnych,
* testach baz danych,
* testach mikroserwisów,
* frameworkach testowych tworzonych wewnętrznie przez zespoły QA.

Przykład testu API:

```python
import requests

def test_healthcheck():
    response = requests.get(
        "https://example.com/health"
    )

    assert response.status_code == 200
```

### Porównanie z unittest

Python posiada wbudowany framework unittest.

Przykład w `unittest`:

```python
import unittest

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(2 + 3, 5)
```

Ten sam test w pytest:

```python
def test_add():
    assert 2 + 3 == 5
```

Dlatego pytest jest często wybierany ze względu na:

* prostszą składnię,
* czytelniejsze testy,
* fixtures,
* łatwą parametryzację,
* bogaty ekosystem pluginów.

### Krótka definicja do notatek

**pytest** – otwartoźródłowy framework do testowania aplikacji w Pythonie, służący do tworzenia i uruchamiania testów
jednostkowych, integracyjnych oraz automatycznych. Oferuje prostą składnię opartą o `assert`, mechanizm fixtures,
parametryzację testów oraz rozbudowany system wtyczek.

## 📕requests

**requests** to jedna z najpopularniejszych bibliotek Pythona służących do wykonywania zapytań HTTP. Umożliwia komunikację
z API, pobieranie danych ze stron internetowych oraz wysyłanie danych do serwerów w prostszy sposób niż standardowe
moduły Pythona.

Biblioteka jest rozwijana jako projekt open source: Requests.

### Czym jest requests?

`requests` jest klientem HTTP dla Pythona.

Pozwala wykonywać m.in. żądania:

* GET
* POST
* PUT
* PATCH
* DELETE
* HEAD
* OPTIONS

Bez konieczności ręcznego zarządzania połączeniami sieciowymi czy nagłówkami HTTP.

### Dlaczego powstało?

Standardowa biblioteka Pythona oferuje moduły takie jak:

```python
urllib
urllib.request
```

Jednak ich użycie jest bardziej rozbudowane.

Przykład:

```python
import requests

response = requests.get(
    "https://api.example.com/users"
)
```

vs.

```python
from urllib.request import urlopen

response = urlopen(
    "https://api.example.com/users"
)
```

Przy bardziej złożonych scenariuszach różnica w czytelności staje się jeszcze większa.

### Instalacja

```bash
pip install requests
```

### Podstawowe użycie

#### GET

```python
import requests

response = requests.get(
    "https://api.example.com/users"
)
```

Odczyt odpowiedzi:

```python
response.status_code
response.text
response.headers
```

#### JSON

Bardzo częsty przypadek w testach API.

```python
response = requests.get(
    "https://api.example.com/users/1"
)

data = response.json()
```

Przykład:

```python
assert data["id"] == 1
```

#### POST

Wysyłanie danych:

```python
payload = {
    "name": "Jan",
    "email": "jan@test.pl"
}

response = requests.post(
    "https://api.example.com/users",
    json=payload
)
```

Biblioteka automatycznie:

* serializuje JSON,
* ustawia odpowiedni nagłówek `Content-Type`.

#### Parametry query

URL:

```text
https://api.example.com/users?page=2&limit=10
```

W requests:

```python
params = {
    "page": 2,
    "limit": 10
}

response = requests.get(
    "https://api.example.com/users",
    params=params
)
```

### Obsługa nagłówków

```python
headers = {
    "Authorization": "Bearer token",
    "Accept": "application/json"
}

response = requests.get(
    url,
    headers=headers
)
```

Często wykorzystywane przy:

* JWT,
* OAuth,
* API Keys.

### Uwierzytelnianie

Basic Auth:

```python
from requests.auth import HTTPBasicAuth

response = requests.get(
    url,
    auth=HTTPBasicAuth(
        "user",
        "password"
    )
)
```

Krócej:

```python
response = requests.get(
    url,
    auth=("user", "password")
)
```

### Timeout

Dobra praktyka w automatyzacji testów.

```python
response = requests.get(
    url,
    timeout=10
)
```

Bez timeoutu test może długo czekać na odpowiedź serwera.

### Obsługa błędów

```python
import requests

try:
    response = requests.get(
        url,
        timeout=5
    )

    response.raise_for_status()

except requests.exceptions.Timeout:
    print("Timeout")

except requests.exceptions.ConnectionError:
    print("Brak połączenia")
```

### Sesje (Session)

Jeżeli wykonujesz wiele zapytań do tego samego systemu:

```python
session = requests.Session()

session.headers.update({
    "Authorization": "Bearer token"
})

response = session.get(url)
```

Korzyści:

* ponowne użycie połączeń TCP,
* wspólne nagłówki,
* wspólne cookies.

### Najważniejsze obiekty

#### Response

Odpowiedź serwera:

```python
response.status_code
response.text
response.json()
response.headers
response.cookies
```

#### Session

Reprezentuje sesję klienta HTTP:

```python
session = requests.Session()
```

### Typowe zastosowania w QA

#### Testy API

```python
def test_get_user():
    response = requests.get(
        "/users/1"
    )

    assert response.status_code == 200
```

#### Testy kontraktowe

Sprawdzenie struktury odpowiedzi:

```python
data = response.json()

assert "id" in data
assert "email" in data
```

#### Health-checki

```python
response = requests.get(
    "/health"
)

assert response.status_code == 200
```

#### Przygotowanie danych testowych

Przed testem UI:

```python
requests.post(
    "/users",
    json=test_user
)
```

Tworzenie danych przez API jest zwykle szybsze niż klikanie ich w interfejsie.

### Współpraca z pytest

Bardzo często `requests` i pytest występują razem.

Przykład:

```python
import requests

def test_user_exists():
    response = requests.get(
        "https://api.example.com/users/1"
    )

    assert response.status_code == 200
```

`pytest` odpowiada za uruchomienie testu i asercje, a `requests` za komunikację HTTP.

### Ograniczenia

`requests`:

* działa synchronicznie,
* nie jest najlepszym wyborem dla bardzo dużej liczby równoległych żądań,
* nie obsługuje natywnie asynchroniczności (`async/await`).

W projektach wymagających wysokiej współbieżności często stosuje się np. HTTPX lub aiohttp.

### Krótka definicja do notatek

**requests** – biblioteka Pythona służąca do wykonywania żądań HTTP (GET, POST, PUT, DELETE itd.) oraz komunikacji
z API i serwerami [WWW](http://WWW). Umożliwia wygodne wysyłanie danych, obsługę odpowiedzi, nagłówków, uwierzytelniania,
sesji i błędów sieciowych. Jest powszechnie wykorzystywana w automatyzacji testów API oraz integracji systemów.

## 📕pydantic

**Pydantic** to biblioteka Pythona służąca do **walidacji, parsowania i serializacji danych** na podstawie adnotacji
typów (type hints). Zamiast ręcznie sprawdzać poprawność danych wejściowych, definiujesz model danych, a Pydantic
automatycznie weryfikuje i konwertuje otrzymane wartości.

Jest szczególnie popularna w aplikacjach backendowych, API oraz frameworku FastAPI, gdzie służy do walidacji danych
przychodzących i wychodzących.

### Czym jest Pydantic?

Najprościej:

> Pydantic pozwala zamienić nieuporządkowane dane (np. JSON z API) na typowane obiekty Pythona z automatyczną walidacją.

Bez Pydantic:

```python
data = {
    "id": "1",
    "name": "Jan"
}

if not isinstance(data["id"], int):
    ...
```

Z Pydantic:

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

user = User(
    id="1",
    name="Jan"
)
```

Pydantic automatycznie przekonwertuje `"1"` na `1`.

### Instalacja

```bash
pip install pydantic
```

### Podstawowy model

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    active: bool
```

Tworzenie obiektu:

```python
user = User(
    id="123",
    name="Jan",
    active="true"
)
```

Wynik:

```python
User(
    id=123,
    name='Jan',
    active=True
)
```

Pydantic potrafi automatycznie konwertować wiele popularnych typów danych.

### Walidacja danych

Jeżeli dane są niepoprawne:

```python
User(
    id="abc",
    name="Jan",
    active=True
)
```

otrzymasz wyjątek:

```python
ValidationError
```

z informacją:

* które pole jest błędne,
* jaka wartość została przekazana,
* jaki typ był oczekiwany.

### Obsługa JSON

Bardzo częsty scenariusz w testach API.

Odpowiedź:

```json
{
  "id": 1,
  "name": "Jan"
}
```

Model:

```python
class User(BaseModel):
    id: int
    name: str
```

Walidacja:

```python
user = User.model_validate(
    response.json()
)
```

Dzięki temu od razu wiadomo, czy API zwróciło dane zgodne z oczekiwanym kontraktem.

### Zagnieżdżone modele

```python
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address
```

Przykład:

```python
user = User(
    id=1,
    name="Jan",
    address={
        "city": "Gdańsk",
        "zip_code": "80-001"
    }
)
```

Pydantic automatycznie utworzy obiekt `Address`.

### Ograniczenia i reguły pól

Można definiować dodatkowe wymagania:

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=50
    )
```

Przykłady:

* minimalna długość,
* maksymalna długość,
* zakres liczb,
* regex,
* wartości obowiązkowe.

### Typy specjalne

Pydantic dostarcza wiele gotowych typów:

```python
from pydantic import EmailStr

class User(BaseModel):
    email: EmailStr
```

Inne przykłady:

* adresy e-mail,
* URL,
* UUID,
* IPv4/IPv6,
* daty i czasy,
* dodatnie liczby (`PositiveInt`).

### Serializacja

Model można łatwo zamienić na słownik:

```python
user.model_dump()
```

wynik:

```python
{
    "id": 1,
    "name": "Jan"
}
```

lub JSON:

```python
user.model_dump_json()
```

### Najczęstsze zastosowania w QA

#### 1. Walidacja odpowiedzi API

```python
class User(BaseModel):
    id: int
    name: str

user = User.model_validate(
    response.json()
)
```

Test przejdzie tylko wtedy, gdy odpowiedź ma poprawną strukturę.

#### 2. Testowanie kontraktów API

Zamiast:

```python
assert "id" in response.json()
assert "name" in response.json()
```

można użyć:

```python
User.model_validate(
    response.json()
)
```

Kod jest krótszy i bardziej czytelny.

#### 3. Dane testowe

```python
test_user = User(
    id=1,
    name="Jan"
)
```

Masz pewność, że dane testowe są poprawne jeszcze przed wysłaniem ich do API.

### Współpraca z pytest i requests

Bardzo często spotykany zestaw:

* pytest – uruchamia testy,
* Requests – wykonuje żądania HTTP,
* Pydantic – waliduje odpowiedzi API.

Przykład:

```python
import requests
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

def test_user():
    response = requests.get(
        "https://api.example.com/users/1"
    )

    user = User.model_validate(
        response.json()
    )

    assert user.id == 1
```

### Dlaczego jest tak popularny?

Główne zalety:

* wykorzystuje type hints,
* eliminuje dużą część ręcznej walidacji,
* generuje czytelne błędy,
* bardzo dobrze współpracuje z IDE,
* potrafi generować schematy JSON Schema,
* jest szybki (rdzeń walidacji napisany w Rust).

### Krótka definicja do notatek

**Pydantic** – biblioteka Pythona służąca do definiowania modeli danych oraz automatycznej walidacji, konwersji
i serializacji danych na podstawie type hints. Jest powszechnie używana do walidacji odpowiedzi API, testów
kontraktowych oraz obsługi danych wejściowych w aplikacjach backendowych.

## 📕Faker

**Faker** to biblioteka Pythona służąca do **generowania realistycznych danych testowych**. Pozwala automatycznie
tworzyć losowe imiona, nazwiska, adresy, numery telefonów, adresy e-mail, daty, numery kart płatniczych, nazwy firm
i wiele innych typów danych.

Jest bardzo popularna w testach automatycznych, seedowaniu baz danych oraz tworzeniu danych testowych do API.

### Czym jest Faker?

Zamiast ręcznie tworzyć dane:

```python
user = {
    "name": "Jan Kowalski",
    "email": "jan.kowalski@test.pl"
}
```

możesz generować je automatycznie:

```python
from faker import Faker

fake = Faker()

user = {
    "name": fake.name(),
    "email": fake.email()
}
```

Przy każdym uruchomieniu otrzymasz nowe, realistyczne dane.

### Instalacja

```bash
pip install faker
```

### Podstawowe użycie

```python
from faker import Faker

fake = Faker()

print(fake.name())
print(fake.email())
print(fake.phone_number())
```

Przykładowy wynik:

```text
Anna Nowak
anna.nowak@example.org
+48 601 123 456
```

### Najczęściej używane generatory

#### Osoby

```python
fake.first_name()
fake.last_name()
fake.name()
```

Przykład:

```text
Jan
Kowalski
Jan Kowalski
```

#### E-mail

```python
fake.email()
fake.company_email()
```

Przykład:

```text
jan.nowak@example.com
```

#### Adres

```python
fake.street_address()
fake.city()
fake.postcode()
fake.address()
```

Przykład:

```text
ul. Lipowa 15
Gdańsk
80-001
```

#### Firma

```python
fake.company()
fake.job()
```

Przykład:

```text
ABC Solutions Sp. z o.o.
QA Engineer
```

#### Internet

```python
fake.user_name()
fake.password()
fake.url()
fake.domain_name()
```

#### Daty

```python
fake.date()
fake.date_of_birth()
fake.future_date()
fake.past_date()
```

#### Liczby

```python
fake.random_int()
fake.pyfloat()
```

### Lokalizacja (locale)

Faker obsługuje wiele języków i krajów.

Polskie dane:

```python
from faker import Faker

fake = Faker("pl_PL")
```

Przykład:

```python
print(fake.name())
print(fake.address())
```

Wynik:

```text
Michał Wiśniewski

ul. Długa 5
80-200 Gdańsk
```

Inne locale:

```python
Faker("en_US")
Faker("de_DE")
Faker("fr_FR")
```

### Powtarzalne dane (seed)

Jeżeli chcesz generować zawsze te same dane:

```python
from faker import Faker

Faker.seed(123)

fake = Faker()

print(fake.name())
```

Przy każdym uruchomieniu wynik będzie identyczny.

Przydatne w testach regresyjnych.

### Generowanie wielu rekordów

```python
for _ in range(5):
    print(
        fake.name(),
        fake.email()
    )
```

Przykład:

```text
Jan Kowalski jan@test.pl
Anna Nowak anna@test.pl
Piotr Zieliński piotr@test.pl
...
```

### Integracja z pytest

Bardzo częsty scenariusz:

```python
from faker import Faker

fake = Faker()

def test_create_user():

    payload = {
        "name": fake.name(),
        "email": fake.email()
    }

    response = client.post(
        "/users",
        json=payload
    )

    assert response.status_code == 201
```

Dzięki temu każdy test używa nowych danych.

### Fixtures w pytest

```python
import pytest
from faker import Faker

@pytest.fixture
def fake():
    return Faker()
```

Użycie:

```python
def test_user(fake):

    email = fake.email()

    assert "@" in email
```

### Typowe zastosowania w QA

#### 1. Tworzenie użytkowników testowych

```python
payload = {
    "name": fake.name(),
    "email": fake.email()
}
```

#### 2. Testowanie walidacji formularzy

```python
fake.email()
fake.phone_number()
fake.postcode()
```

#### 3. Przygotowanie danych do API

```python
response = requests.post(
    "/users",
    json={
        "name": fake.name(),
        "email": fake.email()
    }
)
```

#### 4. Seedowanie bazy danych

```python
for _ in range(1000):
    create_user(
        name=fake.name(),
        email=fake.email()
    )
```

#### 5. Testy obciążeniowe

Generowanie dużej liczby unikalnych rekordów:

```python
fake.uuid4()
fake.email()
fake.user_name()
```

### Zalety

* bardzo szybkie generowanie danych,
* setki gotowych typów danych,
* obsługa wielu krajów i języków,
* łatwa integracja z pytest,
* możliwość generowania realistycznych danych,
* możliwość uzyskania powtarzalnych wyników przez seed.

### Ograniczenia

* dane są realistyczne, ale fikcyjne,
* wygenerowane wartości nie zawsze spełniają wymagania konkretnego systemu,
* czasami trzeba tworzyć własne generatory dla niestandardowych formatów danych.

### Krótka definicja do notatek

**Faker** – biblioteka Pythona służąca do generowania losowych, realistycznych danych testowych, takich jak imiona,
nazwiska, adresy, e-maile, numery telefonów, daty czy dane firmowe. Jest powszechnie wykorzystywana w automatyzacji
testów, przygotowywaniu danych testowych oraz seedowaniu baz danych.

## 📕python-dotenv

**python-dotenv** to biblioteka Pythona służąca do **wczytywania zmiennych środowiskowych z pliku `.env`** do aplikacji.
Dzięki temu można przechowywać konfigurację (np. adresy API, tokeny, hasła, dane dostępowe) poza kodem źródłowym.

### Czym jest python-dotenv?

Zamiast wpisywać dane konfiguracyjne bezpośrednio w kodzie:

```python
API_URL = "https://api.test.com"
API_TOKEN = "secret-token"
```

możesz umieścić je w pliku `.env`:

```text
API_URL=https://api.test.com
API_TOKEN=secret-token
```

a następnie wczytać do aplikacji:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_url = os.getenv("API_URL")
api_token = os.getenv("API_TOKEN")
```

### Dlaczego jest używany?

Pozwala oddzielić:

* kod aplikacji,
* konfigurację środowiska.

Dzięki temu ten sam kod może działać na różnych środowiskach:

* DEV,
* TEST,
* QA,
* STAGE,
* PROD.

Wystarczy zmienić zawartość pliku `.env`.

### Instalacja

```bash
pip install python-dotenv
```

### Podstawowe użycie

#### Plik `.env`

```text
BASE_URL=https://api.test.com
USERNAME=test_user
PASSWORD=test_password
```

#### Kod

```python
from dotenv import load_dotenv
import os

load_dotenv()

base_url = os.getenv("BASE_URL")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
```

### Funkcja `load_dotenv()`

Najczęściej spotykana:

```python
load_dotenv()
```

Domyślnie szuka pliku `.env` w bieżącym katalogu projektu.

### Odczyt zmiennych

```python
import os

os.getenv("BASE_URL")
```

lub:

```python
os.environ["BASE_URL"]
```

Różnica:

```python
os.getenv("BASE_URL")
```

zwraca `None`, gdy zmienna nie istnieje.

Natomiast:

```python
os.environ["BASE_URL"]
```

wyrzuci:

```python
KeyError
```

### Wartości domyślne

```python
timeout = os.getenv(
    "TIMEOUT",
    "30"
)
```

Jeżeli zmienna nie istnieje:

```python
timeout == "30"
```

### Własny plik .env

Można wskazać konkretną lokalizację:

```python
from dotenv import load_dotenv

load_dotenv(".env.qa")
```

Przykład:

```text
.env.dev
.env.qa
.env.prod
```

### Typowy przykład w automatyzacji testów

Plik:

```text
BASE_URL=https://api.qa.company.com
TOKEN=abc123
```

Kod:

```python
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TOKEN = os.getenv("TOKEN")
```

Test:

```python
response = requests.get(
    f"{BASE_URL}/users",
    headers={
        "Authorization": f"Bearer {TOKEN}"
    }
)
```

Dzięki temu nie trzeba zmieniać kodu przy przełączaniu środowisk.

### Integracja z pytest

Bardzo często spotykany wzorzec:

```python
# conftest.py

from dotenv import load_dotenv

load_dotenv()
```

Po uruchomieniu testów wszystkie zmienne są dostępne globalnie:

```python
import os

base_url = os.getenv("BASE_URL")
```

### Przykład z Pydantic

Często używany razem z Pydantic.

```python
from pydantic import BaseModel
import os

class Config(BaseModel):
    base_url: str
    token: str

config = Config(
    base_url=os.getenv("BASE_URL"),
    token=os.getenv("TOKEN")
)
```

Pydantic dodatkowo zweryfikuje poprawność konfiguracji.

### Typowe zastosowania w QA

#### 1. Adresy środowisk

```text
BASE_URL=https://qa.company.com
```

#### 2. Dane logowania

```text
USERNAME=test_user
PASSWORD=secret
```

#### 3. Tokeny API

```text
API_TOKEN=123456
```

#### 4. Parametry testów

```text
TIMEOUT=30
RETRY_COUNT=3
```

#### 5. Konfiguracja baz danych

```text
DB_HOST=localhost
DB_PORT=5432
DB_USER=test
DB_PASSWORD=password
```

### Dobre praktyki

#### Dodaj `.env` do `.gitignore`

Plik może zawierać:

* hasła,
* tokeny,
* klucze API.

Przykład:

```text
.env
.env.*
```

#### Udostępniaj `.env.example`

Przykład:

```text
BASE_URL=
USERNAME=
PASSWORD=
TOKEN=
```

Nowi członkowie zespołu wiedzą wtedy, jakie zmienne są wymagane.

#### Nie przechowuj sekretów w kodzie

Zamiast:

```python
TOKEN = "abc123"
```

lepiej:

```python
TOKEN = os.getenv("TOKEN")
```

### Zalety

* bardzo prosta konfiguracja,
* oddzielenie konfiguracji od kodu,
* łatwe przełączanie środowisk,
* bezpieczniejsze zarządzanie sekretami,
* świetna integracja z pytest i frameworkami webowymi.

### Ograniczenia

* samodzielnie nie szyfruje danych,
* plik `.env` nadal jest zwykłym plikiem tekstowym,
* w dużych organizacjach często zastępowany przez rozwiązania typu:

  * HashiCorp Vault,
  * AWS Secrets Manager,
  * Azure Key Vault.

### Krótka definicja do notatek

**python-dotenv** – biblioteka Pythona umożliwiająca wczytywanie zmiennych środowiskowych z pliku `.env`. Jest
wykorzystywana do przechowywania konfiguracji aplikacji i testów (adresów API, danych logowania, tokenów, parametrów
środowiskowych) poza kodem źródłowym, co ułatwia zarządzanie konfiguracją i zwiększa bezpieczeństwo.

## 📕deepdiff

**DeepDiff** to biblioteka Pythona służąca do **porównywania złożonych struktur danych** i wykrywania różnic między nimi.
Potrafi analizować słowniki (`dict`), listy, obiekty, JSON-y, zagnieżdżone struktury oraz kombinacje tych typów.

### Czym jest DeepDiff?

Załóżmy, że masz dwie odpowiedzi API:

```python
response_1 = {
    "id": 1,
    "name": "Jan",
    "age": 30
}

response_2 = {
    "id": 1,
    "name": "Jan",
    "age": 31
}
```

Standardowo:

```python
assert response_1 == response_2
```

Otrzymasz jedynie informację, że obiekty są różne.

Z DeepDiff:

```python
from deepdiff import DeepDiff

diff = DeepDiff(
    response_1,
    response_2
)

print(diff)
```

Wynik:

```python
{
    'values_changed': {
        "root['age']": {
            'old_value': 30,
            'new_value': 31
        }
    }
}
```

Od razu wiadomo:

* które pole się zmieniło,
* jaka była stara wartość,
* jaka jest nowa wartość.

### Instalacja

```bash
pip install deepdiff
```

### Podstawowe użycie

```python
from deepdiff import DeepDiff

diff = DeepDiff(obj1, obj2)
```

Brak różnic:

```python
{}
```

Wykryte różnice:

```python
{
    ...
}
```

### Porównywanie słowników

```python
from deepdiff import DeepDiff

a = {
    "name": "Jan",
    "age": 30
}

b = {
    "name": "Jan",
    "age": 31
}

DeepDiff(a, b)
```

Wynik:

```python
{
    'values_changed': {
        "root['age']": {
            'old_value': 30,
            'new_value': 31
        }
    }
}
```

### Wykrywanie nowych pól

```python
a = {
    "id": 1
}

b = {
    "id": 1,
    "email": "test@test.pl"
}
```

Wynik:

```python
{
    'dictionary_item_added': [
        "root['email']"
    ]
}
```

### Wykrywanie usuniętych pól

```python
{
    'dictionary_item_removed': [
        "root['email']"
    ]
}
```

### Porównywanie list

```python
a = [1, 2, 3]
b = [1, 2, 4]
```

```python
DeepDiff(a, b)
```

Wynik:

```python
{
    'values_changed': {
        'root[2]': {
            'old_value': 3,
            'new_value': 4
        }
    }
}
```

### Ignorowanie kolejności

Częsty problem w testach API:

```python
a = [1, 2, 3]
b = [3, 2, 1]
```

Standardowo:

```python
a != b
```

DeepDiff:

```python
DeepDiff(
    a,
    b,
    ignore_order=True
)
```

Wynik:

```python
{}
```

### Porównywanie JSON

Ponieważ JSON po deserializacji jest słownikiem:

```python
import requests
from deepdiff import DeepDiff

expected = {
    "id": 1,
    "name": "Jan"
}

actual = response.json()

diff = DeepDiff(
    expected,
    actual
)
```

### Ignorowanie konkretnych pól

Przydatne dla pól dynamicznych:

```python
{
    "id": 1,
    "created_at": "2026-01-01"
}
```

```python
DeepDiff(
    expected,
    actual,
    exclude_paths={
        "root['created_at']"
    }
)
```

Pole zostanie pominięte.

### Ignorowanie wielu pól

```python
exclude_paths={
    "root['id']",
    "root['created_at']",
    "root['updated_at']"
}
```

### Porównywanie typów

```python
a = {
    "age": 30
}

b = {
    "age": "30"
}
```

Wynik:

```python
{
    'type_changes': ...
}
```

DeepDiff wykryje różnicę typu:

```text
int != str
```

### Typowe zastosowania w QA

#### 1. Walidacja odpowiedzi API

```python
diff = DeepDiff(
    expected_response,
    actual_response
)

assert diff == {}
```

#### 2. Testy regresyjne

Porównanie odpowiedzi przed i po zmianach:

```python
old_response
new_response
```

```python
DeepDiff(
    old_response,
    new_response
)
```

#### 3. Testy kontraktowe

Weryfikacja czy struktura odpowiedzi nie uległa zmianie.

#### 4. Porównywanie plików JSON

```python
with open("expected.json") as f:
    expected = json.load(f)

with open("actual.json") as f:
    actual = json.load(f)

DeepDiff(
    expected,
    actual
)
```

#### 5. Porównywanie obiektów Pydantic

Jeżeli używasz Pydantic:

```python
diff = DeepDiff(
    user1.model_dump(),
    user2.model_dump()
)
```

### Integracja z pytest

Przykład:

```python
from deepdiff import DeepDiff

def test_response():

    diff = DeepDiff(
        expected,
        actual,
        ignore_order=True
    )

    assert diff == {}
```

Gdy test nie przejdzie, w logach od razu widać konkretne różnice.

### DeepDiff vs zwykły assert

#### Standardowy assert

```python
assert expected == actual
```

Błąd:

```text
AssertionError
```

Często trudno znaleźć przyczynę.

#### DeepDiff

```python
diff = DeepDiff(
    expected,
    actual
)

assert diff == {}
```

Błąd:

```python
{
    'values_changed': {
        "root['user']['email']": {
            'old_value': 'a@test.com',
            'new_value': 'b@test.com'
        }
    }
}
```

Od razu wiadomo, co się zmieniło.

### Zalety

* obsługuje zagnieżdżone struktury,
* czytelnie raportuje różnice,
* porównuje JSON-y i słowniki,
* pozwala ignorować kolejność elementów,
* umożliwia wykluczanie pól dynamicznych,
* bardzo przydatny w testach API i regresji.

### Ograniczenia

* dla bardzo dużych struktur może być wolniejszy niż zwykłe porównanie,
* nie zastępuje walidacji schematu (do tego lepiej użyć Pydantic lub JSON Schema),
* przy bardzo skomplikowanych obiektach raport może być obszerny.

### Krótka definicja do notatek

**DeepDiff** – biblioteka Pythona służąca do porównywania złożonych struktur danych (słowników, list, JSON-ów i obiektów)
oraz wykrywania szczegółowych różnic między nimi. Jest często wykorzystywana w testach API, regresyjnych i kontraktowych
do analizy zmian w odpowiedziach systemu.

## 📕Pygments

**Pygments** to biblioteka Pythona służąca do **kolorowania składni (syntax highlighting)** kodu źródłowego.
Rozpoznaje składnię wielu języków programowania i formatuje kod w czytelny sposób, np. jako HTML, ANSI
(kolory w terminalu), RTF czy LaTeX.

### Czym jest Pygments?

Kod źródłowy bez kolorowania:

```python
def add(a, b):
    return a + b
```

Po przetworzeniu przez Pygments:

* słowa kluczowe (`def`, `return`) mają inny kolor,
* nazwy funkcji są wyróżnione,
* liczby, stringi i komentarze mają własne style.

Dzięki temu kod jest łatwiejszy do czytania.

### Do czego służy?

Pygments jest wykorzystywany do:

* kolorowania kodu w dokumentacji,
* generowania raportów HTML,
* wyświetlania kodu w terminalu,
* tworzenia stron internetowych z przykładami kodu,
* budowania dokumentacji technicznej.

Wiele narzędzi korzysta z Pygments "pod spodem", np. generatory dokumentacji czy systemy publikujące kod.

### Instalacja

```bash
pip install pygments
```

### Podstawowe użycie

```python
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

code = """
def hello():
    print("Hello")
"""

html = highlight(
    code,
    PythonLexer(),
    HtmlFormatter()
)
```

Wynikiem będzie kod HTML z odpowiednimi znacznikami i klasami CSS odpowiadającymi kolorowaniu składni.

### Najważniejsze elementy

#### Lexer

**Lexer** analizuje kod i rozpoznaje jego elementy, takie jak:

* słowa kluczowe,
* identyfikatory,
* liczby,
* komentarze,
* operatory,
* stringi.

Przykład:

```python
from pygments.lexers import PythonLexer

lexer = PythonLexer()
```

Dla innych języków dostępne są odpowiednie lexery, np.:

```python
from pygments.lexers import JsonLexer
from pygments.lexers import SqlLexer
```

#### Formatter

**Formatter** określa sposób prezentacji pokolorowanego kodu.

Przykłady:

```python
from pygments.formatters import HtmlFormatter
```

lub

```python
from pygments.formatters import TerminalFormatter
```

Najczęściej używane formatery:

* HTML,
* Terminal,
* LaTeX,
* RTF,
* SVG.

### Automatyczne wykrywanie języka

Pygments potrafi sam spróbować rozpoznać język:

```python
from pygments.lexers import guess_lexer

lexer = guess_lexer(code)
```

Jest to wygodne przy pracy z plikami o nieznanej zawartości.

### Kolorowanie w terminalu

```python
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter

print(
    highlight(
        code,
        PythonLexer(),
        TerminalFormatter()
    )
)
```

Kod zostanie wyświetlony z kolorami w terminalu obsługującym sekwencje ANSI.

### Style

Pygments oferuje wiele gotowych motywów kolorystycznych.

Przykład:

```python
formatter = HtmlFormatter(style="monokai")
```

Inne popularne style:

* `default`,
* `friendly`,
* `colorful`,
* `monokai`,
* `native`.

### Obsługiwane języki

Pygments wspiera setki języków i formatów, m.in.:

* Python,
* Java,
* JavaScript,
* TypeScript,
* C,
* C++,
* C#,
* Go,
* Rust,
* SQL,
* HTML,
* CSS,
* XML,
* YAML,
* JSON,
* Bash.

### Typowe zastosowania w QA

Choć Pygments nie jest biblioteką stricte testową, może być używany do:

#### 1. Generowania raportów testowych

Raport HTML może zawierać kolorowane:

* requesty HTTP,
* odpowiedzi API,
* fragmenty kodu,
* stack trace.

#### 2. Dokumentacji frameworka testowego

Przykłady kodu w dokumentacji są czytelniejsze dzięki kolorowaniu składni.

#### 3. Narzędzi wewnętrznych

Przykładowo aplikacja wyświetlająca logi lub pliki konfiguracyjne może używać Pygments do ich estetycznej prezentacji.

### Integracja z innymi bibliotekami

Pygments często współpracuje z:

* Sphinx – generowanie dokumentacji,
* MkDocs – dokumentacja projektów,
* Jupyter – prezentacja kodu w notebookach (w zależności od konfiguracji i użytych komponentów).

### Zalety

* obsługuje setki języków programowania,
* oferuje wiele formatów wyjściowych (HTML, terminal, LaTeX itd.),
* posiada liczne gotowe style kolorowania,
* jest szybki i łatwy w użyciu,
* dobrze integruje się z narzędziami do dokumentacji.

### Ograniczenia

* nie analizuje poprawności kodu – jedynie rozpoznaje jego składnię,
* nie jest formatterem ani linterem,
* jego głównym celem jest poprawa czytelności kodu.

### Czy tester automatyzujący będzie z niego korzystał?

Bezpośrednio – **raczej rzadko**. Większość testerów nie używa Pygments w swoich testach. Można się z nim jednak spotkać
pośrednio, ponieważ jest wykorzystywany przez narzędzia generujące dokumentację, raporty lub prezentujące kod źródłowy.

### Krótka definicja do notatek

**Pygments** – biblioteka Pythona służąca do kolorowania składni kodu źródłowego (syntax highlighting).
Rozpoznaje składnię wielu języków programowania i umożliwia prezentację kodu w różnych formatach, takich jak HTML,
terminal czy LaTeX. Jest szeroko wykorzystywana w narzędziach do dokumentacji, raportowania oraz prezentacji kodu.

## 📕colorama

**Colorama** to biblioteka Pythona służąca do **wyświetlania kolorowego tekstu i formatowania wyjścia w terminalu**.
Umożliwia stosowanie kolorów, jasności tekstu oraz kolorów tła w sposób przenośny między różnymi systemami operacyjnymi,
szczególnie zapewniając poprawne działanie sekwencji ANSI w systemie Windows.

### Czym jest Colorama?

Domyślnie tekst wyświetlany w terminalu wygląda tak:

```python
print("Test zakończony sukcesem")
```

Z Colorama można wyróżnić komunikaty kolorami:

```python
from colorama import Fore

print(Fore.GREEN + "Test zakończony sukcesem")
```

Efekt:

* tekst będzie wyświetlony na zielono.

### Do czego służy?

Colorama jest wykorzystywana do:

* kolorowania komunikatów w terminalu,
* wyróżniania błędów i ostrzeżeń,
* poprawy czytelności logów,
* tworzenia czytelniejszych narzędzi CLI (Command Line Interface).

### Instalacja

```bash
pip install colorama
```

### Inicjalizacja

Najczęściej na początku programu:

```python
from colorama import init

init()
```

W nowszych wersjach biblioteka automatycznie wspiera nowoczesne terminale, jednak wywołanie `init()` nadal jest często
spotykane w starszym kodzie i dla zachowania kompatybilności.

### Kolory tekstu

Import:

```python
from colorama import Fore
```

Przykłady:

```python
print(Fore.RED + "Błąd")
```

```python
print(Fore.GREEN + "Sukces")
```

```python
print(Fore.YELLOW + "Ostrzeżenie")
```

```python
print(Fore.BLUE + "Informacja")
```

Dostępne są m.in.:

* `BLACK`
* `RED`
* `GREEN`
* `YELLOW`
* `BLUE`
* `MAGENTA`
* `CYAN`
* `WHITE`

### Resetowanie koloru

Po zmianie koloru warto go zresetować:

```python
from colorama import Fore

print(Fore.RED + "Błąd" + Fore.RESET)
```

Lub wygodniej:

```python
from colorama import Style

print(Fore.RED + "Błąd" + Style.RESET_ALL)
```

### Kolory tła

Import:

```python
from colorama import Back
```

Przykład:

```python
print(
    Back.YELLOW +
    Fore.BLACK +
    "UWAGA"
)
```

Tekst będzie czarny na żółtym tle.

### Style tekstu

Import:

```python
from colorama import Style
```

Przykład:

```python
print(
    Style.BRIGHT +
    "Ważny komunikat"
)
```

Najczęściej używane:

* `DIM`
* `NORMAL`
* `BRIGHT`
* `RESET_ALL`

### Automatyczny reset

Można włączyć automatyczne resetowanie stylów:

```python
from colorama import init

init(autoreset=True)
```

Wtedy nie trzeba pisać:

```python
Style.RESET_ALL
```

po każdym komunikacie.

### Typowe zastosowania w QA

#### 1. Wyniki testów

```python
from colorama import Fore

print(Fore.GREEN + "PASS")
print(Fore.RED + "FAIL")
```

#### 2. Logowanie

```python
print(Fore.YELLOW + "Wysyłanie requesta...")
```

```python
print(Fore.CYAN + "Odpowiedź API")
```

#### 3. Debugowanie

```python
print(Fore.RED + str(exception))
```

Błędy są od razu widoczne.

#### 4. Własne narzędzia CLI

Przykład:

```text
✓ Wszystkie testy zakończone sukcesem
```

na zielono,

lub

```text
✗ Test zakończony niepowodzeniem
```

na czerwono.

### Integracja z pytest

Colorama nie jest bezpośrednio związana z pytest, ale można jej używać do kolorowania własnych komunikatów:

```python
from colorama import Fore

def test_login():

    print(Fore.CYAN + "Logowanie użytkownika")

    assert True
```

Warto jednak pamiętać, że sam pytest już domyślnie koloruje wyniki testów (`PASSED`, `FAILED`, `ERROR`), więc Colorama
jest przydatna głównie do własnych logów i komunikatów.

### Zalety

* bardzo prosta w użyciu,
* działa na różnych systemach operacyjnych,
* poprawia czytelność logów,
* ułatwia tworzenie estetycznych aplikacji konsolowych,
* dobrze współpracuje z innymi bibliotekami CLI.

### Ograniczenia

* działa wyłącznie w terminalu,
* nie generuje raportów HTML ani PDF,
* odpowiada jedynie za wygląd tekstu, nie za logikę programu.

### Krótka definicja do notatek

**Colorama** – biblioteka Pythona umożliwiająca kolorowanie i formatowanie tekstu wyświetlanego w terminalu.
Zapewnia przenośną obsługę kolorów ANSI (szczególnie na systemie Windows) i jest wykorzystywana do tworzenia
czytelniejszych logów, komunikatów oraz aplikacji konsolowych.

## 📕allure-pytest

**allure-pytest** to wtyczka dla pytest integrująca testy z frameworkiem raportowania Allure Report.
Umożliwia automatyczne zbieranie wyników testów oraz generowanie interaktywnych, czytelnych raportów HTML
zawierających informacje o przebiegu testów, krokach, załącznikach, błędach i statystykach.

### Czym jest allure-pytest?

Domyślny raport pytest wygląda mniej więcej tak:

```text
========================
5 passed
2 failed
========================
```

Po użyciu `allure-pytest` można wygenerować rozbudowany raport zawierający m.in.:

* listę wykonanych testów,
* status każdego testu,
* czas wykonania,
* szczegóły błędów,
* historię uruchomień,
* kroki testowe,
* załączniki (np. logi, zrzuty ekranu, odpowiedzi API),
* wykresy i statystyki.

### Jak działa?

Proces wygląda następująco:

```text
pytest
        │
        ▼
allure-pytest
        │
        ▼
pliki wyników (.json)
        │
        ▼
Allure Report
        │
        ▼
interaktywny raport HTML
```

Sama wtyczka **nie generuje raportu HTML** – zapisuje wyniki testów w formacie zrozumiałym dla Allure Report.

### Instalacja

Instalacja wtyczki:

```bash
pip install allure-pytest
```

Dodatkowo należy zainstalować narzędzie **Allure Report CLI**, które generuje raport HTML z zapisanych wyników.

### Uruchamianie testów

```bash
pytest --alluredir=allure-results
```

Po zakończeniu testów powstanie katalog:

```text
allure-results/
```

zawierający pliki opisujące przebieg testów.

### Generowanie raportu

Po wykonaniu testów:

```bash
allure generate allure-results
```

lub

```bash
allure serve allure-results
```

Polecenie `serve` generuje raport i uruchamia lokalny serwer, otwierając go automatycznie w przeglądarce.

### Podstawowe użycie

Najprostszy test:

```python
def test_login():
    assert True
```

Po uruchomieniu z `--alluredir` zostanie automatycznie uwzględniony w raporcie.

### Opisy testów

Można dodać bardziej czytelne nazwy:

```python
import allure

@allure.title("Logowanie poprawnego użytkownika")
def test_login():
    ...
```

### Opisy funkcjonalności

```python
@allure.feature("Logowanie")
@allure.story("Poprawne logowanie")
def test_login():
    ...
```

Raport grupuje testy według funkcjonalności.

### Severity

Można oznaczyć ważność testów:

```python
@allure.severity(
    allure.severity_level.CRITICAL
)
def test_login():
    ...
```

Dostępne poziomy:

* BLOCKER
* CRITICAL
* NORMAL
* MINOR
* TRIVIAL

### Kroki (Steps)

Jedna z najbardziej przydatnych funkcji.

```python
import allure

@allure.step("Logowanie użytkownika")
def login():
    ...
```

lub:

```python
def test_login():

    with allure.step("Wysłanie requesta"):
        ...

    with allure.step("Sprawdzenie odpowiedzi"):
        ...
```

Raport pokazuje wykonane kroki w kolejności.

### Załączniki

Można dołączać praktycznie dowolne pliki.

Przykład tekstu:

```python
allure.attach(
    response.text,
    name="Response"
)
```

Przykład JSON:

```python
allure.attach(
    json.dumps(
        response.json(),
        indent=4
    ),
    name="Response JSON"
)
```

Można również dołączać:

* screenshoty,
* logi,
* pliki XML,
* pliki PDF,
* nagrania wideo.

### Załączanie screenshotów

Bardzo popularne przy testach UI.

```python
allure.attach.file(
    "screenshot.png",
    name="Screenshot"
)
```

Po nieudanym teście screenshot będzie dostępny bezpośrednio w raporcie.

### Parametry testów

Dla testów parametryzowanych:

```python
@pytest.mark.parametrize(
    "user",
    ["admin", "guest"]
)
def test_login(user):
    ...
```

Raport pokaże osobne wykonanie dla każdego zestawu danych.

### Integracja z pytest

Typowy test:

```python
import allure

@allure.title("Pobranie użytkownika")
def test_get_user():

    with allure.step("Wysłanie requesta"):
        response = requests.get(...)

    with allure.step("Walidacja odpowiedzi"):
        assert response.status_code == 200
```

Każdy krok pojawi się w raporcie.

### Typowe zastosowania w QA

#### 1. Raporty z testów API

Dołączanie:

* requestów,
* response,
* nagłówków,
* logów.

#### 2. Testy UI

Załączanie:

* screenshotów,
* nagrań,
* stack trace.

#### 3. CI/CD

Raport może być generowany automatycznie po każdym uruchomieniu pipeline.

#### 4. Analiza błędów

Dzięki krokom i załącznikom łatwo ustalić:

* co wykonał test,
* na którym etapie nastąpił błąd,
* jaka była odpowiedź systemu.

### Zalety

* bardzo czytelne raporty HTML,
* możliwość dodawania kroków,
* obsługa screenshotów, logów i innych załączników,
* grupowanie testów według funkcjonalności,
* integracja z pytest i pipeline'ami CI/CD,
* statystyki i historia uruchomień.

### Ograniczenia

* wymaga instalacji narzędzia Allure Report CLI do generowania raportów,
* dodanie opisów i kroków wymaga dodatkowych dekoratorów lub wywołań API,
* przy dużej liczbie załączników raport może zajmować dużo miejsca na dysku.

# Krótka definicja do notatek

**allure-pytest** – wtyczka do pytest umożliwiająca integrację z Allure Report. Zbiera wyniki testów i zapisuje je w
formacie wykorzystywanym przez Allure do generowania interaktywnych raportów HTML. Pozwala wzbogacać raporty o kroki
testowe, opisy, poziomy ważności, załączniki (np. logi, odpowiedzi API, zrzuty ekranu) oraz szczegółowe informacje
o przebiegu testów, co ułatwia analizę wyników i diagnozowanie błędów.
