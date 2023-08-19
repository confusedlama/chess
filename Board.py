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
        (1, 2): "wp", 
        (2, 2): "wp", 
        (3, 2): "wp",
        (4, 2): "wp",
        (5, 2): "wp",
        (6, 2): "wp",
        (7, 2): "wp",
        (8, 2): "wp",
        (1, 1): "wr", 
        (2, 1): "wn", 
        (3, 1): "wb",
        (4, 1): "wq",
        (5, 1): "wk",
        (6, 1): "wb",
        (7, 1): "wn",
        (8, 1): "wr"
      }
      
      self.black_pieces = {
        (1, 7): "bp", 
        (2, 7): "bp", 
        (3, 7): "bp",
        (4, 7): "bp",
        (5, 7): "bp",
        (6, 7): "bp",
        (7, 7): "bp",
        (8, 7): "bp",
        (1, 8): "br", 
        (2, 8): "bn", 
        (3, 8): "bb",
        (4, 8): "bq",
        (5, 8): "bk",
        (6, 8): "bb",
        (7, 8): "bn",
        (8, 8): "br"
      }
    else:
      self.white_pieces = None
      self.black_pieces = None