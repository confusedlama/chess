class Board():

    """
      8 ▢▢▢▢▢▢▢▢
        ▢▢▢▢▢▢▢▢
      . ▢▢▢▢▢▢▢▢
      . ▢▢▢▢▢▢▢▢
      . ▢▢▢▢▢▢▢▢
        ▢▢▢▢▢▢▢▢
        ▢▢▢▢▢▢▢▢
      1 ▢▢▢▢▢▢▢▢
        1    ...   8
       (a    ...   h)
    """
    # only for initializing a board
    def __init__(self) -> None:
        self.white_pieces = {
                (1, 2): "pawn", 
                (2, 2): "pawn", 
                (3, 2): "pawn",
                (4, 2): "pawn",
                (5, 2): "pawn",
                (6, 2): "pawn",
                (7, 2): "pawn",
                (8, 2): "pawn",
                (1, 1): "rook", 
                (2, 1): "knight", 
                (3, 1): "bishop",
                (4, 1): "queen",
                (5, 1): "king",
                (6, 1): "bishop",
                (7, 1): "knight",
                (8, 1): "rook"
            }
        
        self.black_pieces = {
                (1, 7): "pawn", 
                (2, 7): "pawn", 
                (3, 7): "pawn",
                (4, 7): "pawn",
                (5, 7): "pawn",
                (6, 7): "pawn",
                (7, 7): "pawn",
                (8, 7): "pawn",
                (1, 8): "rook", 
                (2, 8): "knight", 
                (3, 8): "bishop",
                (4, 8): "queen",
                (5, 8): "king",
                (6, 8): "bishop",
                (7, 8): "knight",
                (8, 8): "rook"
        }