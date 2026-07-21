import json
from json import JSONDecodeError

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import JsonLexer

from loggers.console_colors import yellow


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# NOTE FOR ME:
# Java-owa metoda nazywała się {print}, ale w Pythonie {print} to wbudowana funkcja - nazwanie tak własnej
# funkcji przysłoniłoby ją w tym module (nie moglibyśmy już użyć wbudowanego {print(...)} niżej w kodzie).
# Stąd {print_json} zamiast {print}.
def print_json(json_text: str, color_enabled: bool) -> None:
    try:
        parsed = json.loads(json_text)
    except JSONDecodeError:
        # NOTE FOR ME: Tak jak w Javie - ostrzeżenie, tylko gdy {color_enabled}, ale surowy tekst zawsze.
        if color_enabled:
            yellow("Invalid JSON. Display as text:", color_enabled)
        print(json_text)
        return

    # NOTE FOR ME: {indent=2} odpowiada Javowemu {"  ".repeat(level)} (2 spacje na poziom zagnieżdżenia).
    formatted = json.dumps(parsed, ensure_ascii=False, indent=2)

    if color_enabled:
        # NOTE FOR ME: {end=""} bo {highlight()} z Pygments sam dokleja już jeden znak nowej linii na końcu -
        # bez tego mielibyśmy podwójny odstęp względem wersji bez koloru.
        print(highlight(formatted, JsonLexer(), TerminalFormatter()), end="")
    else:
        print(formatted)
