class Piece():
    def __init__(self, position:list, player:int) -> None:
        self.position = position
        self.player = player
    
class King(Piece):
    def __init__(self, position: list, player:int) -> None:
        super().__init__(position, player)
        self.type = "k"
        self.type_long = "King"

    # returns all reachable positions does not take other pieces into account that might block the way
    def get_moves(self) -> list:
        possible_moves = [
            [self.position[0]-1, self.position[1]-1],
            [self.position[0], self.position[1]-1],
            [self.position[0]+1, self.position[1]-1],
            [self.position[0]-1, self.position[1]],
            [self.position[0]+1, self.position[1]],
            [self.position[0]-1, self.position[1]+1],
            [self.position[0], self.position[1]+1],
            [self.position[0]+1, self.position[1]+1],
        ]

        moves = []

        for move in possible_moves:
            if move[0] > 0 and move[0] < 9 and move[1] > 0 and move[1] < 9:
                moves.append(move)

        return moves

class Queen(Piece):
    def __init__(self, position: list, player: int) -> None:
        super().__init__(position, player)

    def get_moves(self) -> list:
        moves = []

        # straights
        for i in range(1, self.position[0]):
            moves.append([i, self.position[1]])
        for i in range(self.position[0]+1 , 9):
            moves.append([i, self.position[1]])
        for i in range(1, self.position[1]):
            moves.append([self.position[0], i])
        for i in range(self.position[1]+1 , 9):
            moves.append([self.position[0], i])

        # for kleinere kathete von der diagonale append pos
        # diagonals
        if self.position[0] < 8 - self.position[1]:
            for i in range(self.position[0]):
                moves.append([self.position[0]-i, self.position[1]+i])
        if self.position[0] < self.position[1]:
            for i in range(self.position[0]):
                moves.append([self.position[0]-i, self.position[1]-i])
        return moves
    
class Rook(Piece):
    def __init__(self, position: list, player: int) -> None:
        super().__init__(position, player)

    def get_moves(self) -> list:
        moves = []

        for i in range(1, self.position[0]):
            moves.append([i, self.position[1]])
        for i in range(self.position[0]+1 , 9):
            moves.append([i, self.position[1]])
        for i in range(1, self.position[1]):
            moves.append([self.position[0], i])
        for i in range(self.position[1]+1 , 9):
            moves.append([self.position[0], i])

        return moves


queen = Queen([1,1], 0)
print(queen.get_moves())
# print(list(range(1, 1)))