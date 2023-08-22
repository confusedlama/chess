from Board import Board
from Piece import Queen, King, Bishop, Knight, Rook, Pawn


def make_player_map(board:Board):
    return {
        0: board.white_pieces,
        1: board.black_pieces
    }


class game:
    def __init__(self) -> None:
        self.board = Board()
        self.turn = 0
        self.pieces_map = make_player_map(self.board)

    def get_current_player_pieces(self) -> dict:
        return self.pieces_map[self.turn % 2]
    
    def get_opposing_player_pieces(self) -> dict:
        return self.pieces_map[(self.turn + 1) % 2]
    
    # creates a copy of the board and moves the piece on it, but doesnt effect the game state in any way!!!
    def move_piece(self, piece_x, piece_y, goal_x, goal_y) -> Board:
        # copy board
        new_board = self.board.copy_board()
        new_pieces_map = make_player_map(new_board)

        # move piece on new board
        active_piece = new_pieces_map[self.turn % 2][(piece_x, piece_y)]
        new_pieces_map[self.turn % 2].pop((piece_x, piece_y))
        new_pieces_map[self.turn % 2][(goal_x, goal_y)] = active_piece

        return new_board, new_pieces_map

    def gui_move(self, piece_x, piece_y, goal_x, goal_y):
        if self.is_legal(piece_x, piece_y, goal_x, goal_y):
            self.board, self.pieces_map = self.move_piece(piece_x, piece_y, goal_x, goal_y)
            self.turn += 1
            # print("legal")
        else:
            # print("not legal")
            pass

    # Vorbedingung:
    # auf piece_x, piece_y steht eine figur
    def is_legal(self, piece_x, piece_y, goal_x, goal_y):
        # goal pos is on board
        if 0 < goal_x and goal_x < 9 and 0 < goal_y and goal_y < 9:
            # print("goal pos is on board")
            # piece owned by player who has to move
            if (piece_x, piece_y) in self.get_current_player_pieces():
                # print("piece is in active team")
                # goal is in moveset
                if (goal_x, goal_y) in self.get_current_player_pieces()[(piece_x, piece_y)].get_moves(piece_x, piece_y):
                    # print("goal is in piece moveset")
                    return True
        return False
            