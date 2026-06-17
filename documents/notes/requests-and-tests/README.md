# 🌐Requests i testy – notatki

# 📑Spis treści

- [START – rozpoczęcie pisania testów](#start--rozpoczęcie-pisania-testów)
  - [Dostępy](#dostępy)
  - [config.ini](#configini)
  - [.env](#env)
  - [config.py](#configpy)

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
   allureReport=true
   
   # BASE URL
   baseUrl=https://api.trello.com/1
   # If you want use string builder
   baseUrlProtocol=https
   baseUrlSubdomain=api
   baseUrlDomain=trello
   baseUrlTLD=com
   baseUrlNumber=1
   ```

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
