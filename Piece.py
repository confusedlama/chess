

class Piece():
    def __init__(self, player:str, type:str) -> None:
        self.player = player
        self.type = type


class King(Piece):
    def __init__(self, player:str, type:str) -> None:
        super().__init__(player, type)
        self.has_moved = False

    # returns all reachable positions does not take other pieces into account that might block the way
    def get_moves(self, x, y) -> dict:
        return {
            (x-1, y-1),
            (x, y-1),
            (x+1, y-1),
            (x-1, y),
            (x+1, y),
            (x-1, y+1),
            (x, y+1),
            (x+1, y+1),
        }


class Queen(Piece):
    def __init__(self, player:str, type:str) -> None:
        super().__init__(player, type)

    def get_moves(self, x, y) -> list:
        return {
            (x+1, y),
            (x+2, y),
            (x+3, y),
            (x+4, y),
            (x+5, y),
            (x+6, y),
            (x+7, y),
            (x-1, y),
            (x-2, y),
            (x-3, y),
            (x-4, y),
            (x-5, y),
            (x-6, y),
            (x-7, y),
            (x, y+1),
            (x, y+2),
            (x, y+3),
            (x, y+4),
            (x, y+5),
            (x, y+6),
            (x, y+7),
            (x, y-1),
            (x, y-2),
            (x, y-3),
            (x, y-4),
            (x, y-5),
            (x, y-6),
            (x, y-7),
            (x+1, y+1),
            (x+2, y+2),
            (x+3, y+3),
            (x+4, y+4),
            (x+5, y+5),
            (x+6, y+6),
            (x+7, y+7),
            (x-1, y-1),
            (x-2, y-2),
            (x-3, y-3),
            (x-4, y-4),
            (x-5, y-5),
            (x-6, y-6),
            (x-7, y-7),
            (x-1, y+1),
            (x-2, y+2),
            (x-3, y+3),
            (x-4, y+4),
            (x-5, y+5),
            (x-6, y+6),
            (x-7, y+7),
            (x+1, y-1),
            (x+2, y-2),
            (x+3, y-3),
            (x+4, y-4),
            (x+5, y-5),
            (x+6, y-6),
            (x+7, y-7)
        }


class Rook(Piece):
    def __init__(self, player:str, type:str) -> None:
        super().__init__(player, type)
        self.has_moved = False

    def get_moves(self, x, y) -> list:
                return {
            (x+1, y),
            (x+2, y),
            (x+3, y),
            (x+4, y),
            (x+5, y),
            (x+6, y),
            (x+7, y),
            (x-1, y),
            (x-2, y),
            (x-3, y),
            (x-4, y),
            (x-5, y),
            (x-6, y),
            (x-7, y),
            (x, y+1),
            (x, y+2),
            (x, y+3),
            (x, y+4),
            (x, y+5),
            (x, y+6),
            (x, y+7),
            (x, y-1),
            (x, y-2),
            (x, y-3),
            (x, y-4),
            (x, y-5),
            (x, y-6),
            (x, y-7)
        }


class Bishop(Piece):
    def __init__(self, player:str, type:str) -> None:
        super().__init__(player, type)
        
    def get_moves(self, x, y) -> list:
        return {
            (x+1, y+1),
            (x+2, y+2),
            (x+3, y+3),
            (x+4, y+4),
            (x+5, y+5),
            (x+6, y+6),
            (x+7, y+7),
            (x-1, y-1),
            (x-2, y-2),
            (x-3, y-3),
            (x-4, y-4),
            (x-5, y-5),
            (x-6, y-6),
            (x-7, y-7),
            (x-1, y+1),
            (x-2, y+2),
            (x-3, y+3),
            (x-4, y+4),
            (x-5, y+5),
            (x-6, y+6),
            (x-7, y+7),
            (x+1, y-1),
            (x+2, y-2),
            (x+3, y-3),
            (x+4, y-4),
            (x+5, y-5),
            (x+6, y-6),
            (x+7, y-7)
        }


class Knight(Piece):
    def __init__(self, player:str, type:str) -> None:
        super().__init__(player, type)
        
    def get_moves(self, x, y) -> list:
        return {
            (x+1, y-2),
            (x-1, y-2),
            (x+1, y+2),
            (x-1, y+2),
            (x+2, y-1),
            (x+2, y+1),
            (x-2, y-1),
            (x-2, y+1)
        }


class Pawn(Piece):
    def __init__(self, player:str, type:str) -> None:
        super().__init__(player, type)
        self.has_moved = False
        
    def get_moves(self, x, y) -> list:
        if self.player == "w":
            return {
                (x, y+1)
            }
        else:
            return {
                (x, y-1)
            }
