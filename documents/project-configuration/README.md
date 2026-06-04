# 🛠️Konfiguracja projektu – notatki

# 📑Spis treści

1. [🔧Konfiguracja](#konfiguracja)
   - [Python – Instalacja](#python--instalacja)
   - [IDE PyCharm  – Instalacja](#ide-pycharm--instalacja)
   - [GitHub – Tworzenie i klonowanie repozytorium](#github--tworzenie-i-klonowanie-repozytorium)
2. [🧩Dodatkowe](#dodatkowe)
   - [✔️Typo — Poprawienie błędów w tekście dla plików (głównie Markdown) pisanych w języku polskim](#typo--poprawienie-błędów-w-tekście-dla-plików-głównie-markdown-pisanych-w-języku-polskim)
   - [⬇️Markdown — wyłączenie podkreślania błędów we fragmentach kodu](#markdown--wyłączenie-podkreślania-błędów-we-fragmentach-kodu)
3. [🔌Pluginy do IDE](#pluginy-do-ide)
   - [Rainbow Brackets](#rainbow-brackets)
   - [Allure Report](#allure-report)

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

# 🧩Dodatkowe

## ✔️Typo — Poprawienie błędów w tekście dla plików (głównie Markdown) pisanych w języku polskim

1. Klikamy `Hamburger Menu` w lewym, górnym rogu
2. Klikamy `File`
3. Klikamy `Settings`
4. Rozwijamy `Editor`
5. Klikamy `Natural Languages`
6. Klikamy `+`
7. Szukamy na liście `Polski`
8. Klikamy `Apply`
9. Klikamy `OK`

## ⬇️Markdown — wyłączenie podkreślania błędów we fragmentach kodu

1. Dodajemy blok kodu z błędem np. `print("czesć World")`
2. Najeżdżamy kursorem na podkreślone słowo `czesć`
3. Po najechaniu powinno pojawić się okno z propozycją poprawy
4. Klikamy `More actions...`
5. Klikamy `Hide problems in code fences`  
   Po najechaniu na tę opcję widzimy podpowiedź, że dotyczy to tylko **Markdown**
6. Gdybyśmy chcieli to cofnąć to komunikat podpowie nam takie coś:  
   `Problem highlighting for fenced code blocks in Markdown is disabled. You can enable it in the settings under Languages and Frameworks | Markdown.`
7. Może być tak, że Git będzie chciał dodać i pushnąć plik `markdown.xml`. Dodajemy i pushujemy

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
2️⃣ W **dolnym panelu IntelliJ** przejdź do zakładki **"Allure"**.  
3️⃣ Kliknij **"Generate Report"**, aby zobaczyć wyniki w IDE.  
4️⃣ Możesz nawigować po testach, sprawdzać błędy i załączniki.

### **📢 Zalety wtyczki Allure Report**
🚀 **Nie trzeba otwierać raportów w przeglądarce** – wszystko działa w IDE.  
🔍 **Szybki podgląd wyników testów** bez dodatkowych poleceń w terminalu.  
📊 **Wizualizacja błędów, logów i statystyk** testów.  
🛠️ **Łatwa integracja z popularnymi frameworkami** testowymi.

Jeśli pracujesz z Allure, ta wtyczka **znacznie ułatwia życie**! 🔥
