from Piece import Queen, King, Bishop, Knight, Rook, Pawn


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
  def __init__(self, parent=None) -> None:
    if parent == None:
      self.white_pieces = {
        (1, 2): Pawn((1, 2), "w", "p"), 
        (2, 2): Pawn((2, 2), "w", "p"), 
        (3, 2): Pawn((3, 2), "w", "p"),
        (4, 2): Pawn((4, 2), "w", "p"),
        (5, 2): Pawn((5, 2), "w", "p"),
        (6, 2): Pawn((6, 2), "w", "p"),
        (7, 2): Pawn((7, 2), "w", "p"),
        (8, 2): Pawn((8, 2), "w", "p"),
        (1, 1): Rook((1, 1), "w", "r"), 
        (2, 1): Knight((2, 1), "w", "n"), 
        (3, 1): Bishop((3, 1), "w", "b"),
        (4, 1): Queen((4, 1), "w", "q"),
        (5, 1): King((5, 1), "w", "k"),
        (6, 1): Bishop((6, 1), "w", "b"),
        (7, 1): Knight((7, 1), "w", "n"),
        (8, 1): Rook((8, 1), "w", "r")
      }
      
      self.black_pieces = {
        (1, 7): Pawn((1, 7), "b", "p"), 
        (2, 7): Pawn((2, 7), "b", "p"), 
        (3, 7): Pawn((3, 7), "b", "p"),
        (4, 7): Pawn((4, 7), "b", "p"),
        (5, 7): Pawn((5, 7), "b", "p"),
        (6, 7): Pawn((6, 7), "b", "p"),
        (7, 7): Pawn((7, 7), "b", "p"),
        (8, 7): Pawn((8, 7), "b", "p"),
        (1, 8): Rook((1, 8), "b", "r"), 
        (2, 8): Knight((2, 8), "b", "n"), 
        (3, 8): Bishop((3, 8), "b", "b"),
        (4, 8): Queen((4, 8), "b", "q"),
        (5, 8): King((5, 8), "b", "k"),
        (6, 8): Bishop((6, 8), "b", "b"),
        (7, 8): Knight((7, 8), "b", "n"),
        (8, 8): Rook((8, 8), "b", "r")
      }
    else:
      self.white_pieces = None
      self.black_pieces = None