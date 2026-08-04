from dataclasses import dataclass


# ==========================================================================================================
# DTO
# ==========================================================================================================

# NOTE FOR ME:
# Odpowiednik Javowego {AllureAttachment} - prosty, niemutowalny nośnik danych między
# {allure_formatter.format_attachment()} a miejscem, gdzie załącznik trafia do Allure ({http_logger.log()}).
# Java ma tu klasę z {final} polami; w Pythonie odpowiednikiem jest {@dataclass}
# (ten sam wzorzec co {MaskedRequest} w {utils_sensitive_data_masker.py}).
@dataclass(kw_only=True)
class AllureAttachment:
    title: str
    content: str
