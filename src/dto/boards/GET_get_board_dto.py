from dto.boards.board_base_dto import BoardBaseDto


class GET_GetBoardDto(BoardBaseDto):
    """
    NOTE FOR ME:
    Brak nowych pól względem BoardBaseDto - w Javie GET_GetBoardDto i tak musiał
    powtórzyć cały konstruktor nadklasy (wymóg @JsonCreator per klasa).
    W Pydantic konstruktor jest generowany automatycznie z sumy pól całej hierarchii,
    więc przy braku nowych pól/nadpisań ta klasa nie potrzebuje żadnej dodatkowej
    zawartości - samo dziedziczenie po BoardBaseDto wystarcza.
    """
    pass
