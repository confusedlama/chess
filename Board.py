from Piece import Queen, King, Bishop, Knight, Rook, Pawn
import copy

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

  # parent should point at previous position
  # children will eventually point at the following positions
  def __init__(self, parent=None, debug=None) -> None:
    self.parent = parent
    self.children = []


    if not parent == None:
      self.white_pieces = copy.deepcopy(parent.white_pieces)
      self.black_pieces = copy.deepcopy(parent.black_pieces)
    else:
      if parent == None and debug == None:
        self.white_pieces = {
          (1, 2): Pawn("w", "p"), 
          (2, 2): Pawn("w", "p"), 
          (3, 2): Pawn("w", "p"),
          (4, 2): Pawn("w", "p"),
          (5, 2): Pawn("w", "p"),
          (6, 2): Pawn("w", "p"),
          (7, 2): Pawn("w", "p"),
          (8, 2): Pawn("w", "p"),
          (1, 1): Rook("w", "r"), 
          (2, 1): Knight("w", "n"), 
          (3, 1): Bishop("w", "b"),
          (4, 1): Queen("w", "q"),
          (5, 1): King("w", "k"),
          (6, 1): Bishop("w", "b"),
          (7, 1): Knight("w", "n"),
          (8, 1): Rook("w", "r")
        }
        
        self.black_pieces = {
          (1, 7): Pawn("b", "p"), 
          (2, 7): Pawn("b", "p"), 
          (3, 7): Pawn("b", "p"),
          (4, 7): Pawn("b", "p"),
          (5, 7): Pawn("b", "p"),
          (6, 7): Pawn("b", "p"),
          (7, 7): Pawn("b", "p"),
          (8, 7): Pawn("b", "p"),
          (1, 8): Rook("b", "r"), 
          (2, 8): Knight("b", "n"), 
          (3, 8): Bishop("b", "b"),
          (4, 8): Queen("b", "q"),
          (5, 8): King("b", "k"),
          (6, 8): Bishop("b", "b"),
          (7, 8): Knight("b", "n"),
          (8, 8): Rook("b", "r")
        }
      elif debug == "king":
        self.white_pieces = {
          (8, 8): King("w", "k")
        }
        self.black_pieces = {
          (1, 1): King("b", "k")
        }
      else:
        raise NotImplementedError

  def copy_board(self):
    child = Board(parent=self)
    self.children.append(child)
    return child
