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
   - **assertpy** – Czytelniejsze asercje (`pip install assertpy`)
   - **python-dotenv** – Odczytywanie danych z pliku `.env` (`pip install python-dotenv`)
   - **deepdiff** – Rekurencyjne porównywanie danych (`pip install deepdiff`)
   - Można też zainstalować wszystko naraz jednym poleceniem:
     ```bash
     pip install pytest requests pydantic Faker assertpy python-dotenv deepdiff
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

## 📕assertpy

**assertpy** to biblioteka Pythona dostarczająca **bardziej czytelne i ekspresyjne asercje** niż standardowy `assert`.
Pozwala pisać testy w stylu tzw. *fluent assertions* (łańcuchowych asercji), dzięki czemu kod testów jest często
łatwiejszy do czytania i bliższy językowi naturalnemu.

### Czym jest assertpy?

Standardowa asercja w Pythonie:

```python
assert user["name"] == "Jan"
```

W assertpy:

```python
from assertpy import assert_that

assert_that(user["name"]).is_equal_to("Jan")
```

Oba zapisy robią to samo, ale drugi jest bardziej opisowy.

### Instalacja

```bash
pip install assertpy
```

### Podstawowe użycie

Import:

```python
from assertpy import assert_that
```

Przykład:

```python
assert_that(5).is_equal_to(5)
```

### Najczęściej używane asercje

#### Porównanie wartości

```python
assert_that(10).is_equal_to(10)
```

```python
assert_that(10).is_not_equal_to(5)
```

#### Wartości logiczne

```python
assert_that(True).is_true()
```

```python
assert_that(False).is_false()
```

#### None

```python
assert_that(user).is_not_none()
```

```python
assert_that(value).is_none()
```

#### Stringi

```python
assert_that("Jan Kowalski").contains("Jan")
```

```python
assert_that("Jan Kowalski").starts_with("Jan")
```

```python
assert_that("Jan Kowalski").ends_with("Kowalski")
```

```python
assert_that("Jan").is_length(3)
```

#### Listy i kolekcje

```python
assert_that(users).contains("Jan")
```

```python
assert_that(users).does_not_contain("Adam")
```

```python
assert_that(users).is_not_empty()
```

```python
assert_that(users).is_length(3)
```

#### Słowniki

```python
assert_that(response).contains_key("id")
```

```python
assert_that(response).contains_value("Jan")
```

```python
assert_that(response).contains_entry({
    "id": 1
})
```

### Łańcuchowanie asercji

Jedna z największych zalet.

```python
assert_that(email) \
    .is_not_empty() \
    .contains("@") \
    .ends_with(".com")
```

Dzięki temu można opisać wiele oczekiwań wobec jednej wartości.

### Obsługa wyjątków

Sprawdzanie wyjątków:

```python
from assertpy import assert_that

assert_that(
    lambda: int("abc")
).raises(ValueError)
```

### Przykłady w testach API

Odpowiedź:

```python
data = response.json()
```

Standardowo:

```python
assert data["id"] == 1
assert data["name"] == "Jan"
assert "email" in data
```

W assertpy:

```python
assert_that(data["id"]).is_equal_to(1)

assert_that(data["name"]).is_equal_to("Jan")

assert_that(data).contains_key("email")
```

### Integracja z pytest

Bardzo często używany razem z pytest.

```python
from assertpy import assert_that

def test_sum():
    result = 2 + 3

    assert_that(result).is_equal_to(5)
```

Pytest uruchamia test, a assertpy odpowiada za bardziej czytelne asercje.

### Przykład z requests i pydantic

```python
from assertpy import assert_that

user = User.model_validate(
    response.json()
)

assert_that(user.id).is_positive()

assert_that(user.name).is_not_empty()
```

W połączeniu z:

* Requests,
* Pydantic,
* pytest

tworzy bardzo czytelne testy API.

### Zalety

#### Czytelność

```python
assert_that(price).is_greater_than(0)
```

jest często bardziej zrozumiałe niż:

```python
assert price > 0
```

#### Bogaty zestaw metod

Dla:

* stringów,
* list,
* słowników,
* liczb,
* wyjątków,
* dat.

#### Fluent API

Możliwość łańcuchowania:

```python
assert_that(name) \
    .is_not_empty() \
    .starts_with("J")
```

#### Lepsza komunikacja intencji testu

Kod przypomina opis wymagań biznesowych.

### Ograniczenia

* dodaje dodatkową zależność do projektu,
* większość prostych testów można napisać zwykłym `assert`,
* nie jest tak powszechnie używany jak natywne asercje pytest.

W wielu zespołach spotkasz wyłącznie:

```python
assert response.status_code == 200
```

ponieważ pytest już sam generuje bardzo dobre komunikaty o błędach.

### assertpy vs standardowy assert

#### Standardowy pytest

```python
assert user.age > 18
```

#### assertpy

```python
assert_that(user.age).is_greater_than(18)
```

#### Standardowy pytest

```python
assert "email" in response
```

#### assertpy

```python
assert_that(response).contains_key("email")
```

Assertpy stawia przede wszystkim na **czytelność i opisowość**, a nie na dodawanie nowych możliwości testowych.

### Krótka definicja do notatek

**assertpy** – biblioteka Pythona dostarczająca fluent assertions (łańcuchowe asercje), umożliwiająca tworzenie
bardziej czytelnych i opisowych testów niż standardowy `assert`. Oferuje bogaty zestaw metod do weryfikacji liczb,
tekstów, kolekcji, słowników i wyjątków oraz dobrze integruje się z pytest.

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

## deepdiff

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
