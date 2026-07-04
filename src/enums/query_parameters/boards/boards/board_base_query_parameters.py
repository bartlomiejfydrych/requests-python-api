from enums.query_parameters.base_query_parameter import BaseQueryParameter


class BoardBaseQueryParameters(BaseQueryParameter):
    """
    NOTES FOR ME:
    Implementuje strukturalnie PostCreateBoardQueryParam i PutUpdateBoardQueryParam
    (przez odziedziczone property {key} z BaseQueryParameter).
    """

    # -----------------------
    # COMMON QUERY PARAMETERS
    # -----------------------

    NAME = "name"
    DESC = "desc"
    ID_ORGANIZATION = "idOrganization"
