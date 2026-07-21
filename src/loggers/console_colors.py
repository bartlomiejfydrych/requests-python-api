from colorama import init as colorama_init, Fore, Style

# NOTE FOR ME:
# {init()} patchuje {sys.stdout}, żeby kody ANSI działały też w starym Windowsowym {cmd.exe} / niektórych CI.
# Wołane raz, przy imporcie tego modułu (Python i tak cache'uje importy, więc nie odpali się drugi raz).
# W Javie ten problem nie był realnie rozwiązany (brak {AnsiConsole.systemInstall()}) - tutaj świadomie
# robimy to lepiej, bo koszt jest znikomy (1 import + 1 wywołanie), a zysk to realna przenośność.
colorama_init()


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

def green(text: str, enabled: bool) -> None:
    _print(text, Fore.GREEN, enabled)


def purple(text: str, enabled: bool) -> None:
    _print(text, Fore.MAGENTA, enabled)


def cyan(text: str, enabled: bool) -> None:
    _print(text, Fore.CYAN, enabled)


def yellow(text: str, enabled: bool) -> None:
    _print(text, Fore.YELLOW, enabled)


# ==========================================================================================================
# METHODS – SUB
# ==========================================================================================================

def _print(text: str, color: str, enabled: bool) -> None:
    if enabled:
        print(f"{color}{text}{Style.RESET_ALL}")
    else:
        print(text)
