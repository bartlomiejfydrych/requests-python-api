from configuration.config import (
    get_base_url_protocol,
    get_base_url_subdomain,
    get_base_url_domain,
    get_base_url_tld,
    get_base_url_number,
)


def build_base_url() -> str:
    return "{}://{}.{}.{}/{}".format(
        get_base_url_protocol(),
        get_base_url_subdomain(),
        get_base_url_domain(),
        get_base_url_tld(),
        get_base_url_number(),
    )
