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
   - Można też zainstalować wszystko naraz jednym poleceniem:
     ```bash
     pip install pytest requests pydantic Faker assertpy
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
