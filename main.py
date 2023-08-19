from os.path import join
import pygame as pg
from Board import Board


def gui_to_logic_pos(pos_x, pos_y):
    return ((pos_x // 75) + 1, 8 - ((pos_y - 100) // 75))

def logic_to_gui_pos(pos_x, pos_y):
    return ((pos_x - 1) * 75, (8 - (pos_y)) * 75 + 100)

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((600, 700))
    clock = pg.time.Clock()
    running = True
    pg.display.set_caption('chess')

    board_image = pg.image.load("board.png").convert()
    pieces_dir = "pieces"
    
    piece_images = {
        "bb": pg.image.load(join(pieces_dir, "bb.png")).convert_alpha(),
        "bk": pg.image.load(join(pieces_dir, "bk.png")).convert_alpha(),
        "bn": pg.image.load(join(pieces_dir, "bn.png")).convert_alpha(),
        "bp": pg.image.load(join(pieces_dir, "bp.png")).convert_alpha(),
        "bq": pg.image.load(join(pieces_dir, "bq.png")).convert_alpha(),
        "br": pg.image.load(join(pieces_dir, "br.png")).convert_alpha(),
        "wb": pg.image.load(join(pieces_dir, "wb.png")).convert_alpha(),
        "wk": pg.image.load(join(pieces_dir, "wk.png")).convert_alpha(),
        "wn": pg.image.load(join(pieces_dir, "wn.png")).convert_alpha(),
        "wp": pg.image.load(join(pieces_dir, "wp.png")).convert_alpha(),
        "wq": pg.image.load(join(pieces_dir, "wq.png")).convert_alpha(),
        "wr": pg.image.load(join(pieces_dir, "wr.png")).convert_alpha()
    }

    board = Board()

    active_piece_position = None

    while running:
        # poll for events
        # pg.QUIT event means the user clicked X to close your window
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                klicked_pos = gui_to_logic_pos(event.pos[0], event.pos[1])
                if klicked_pos in board.white_pieces.keys() or klicked_pos in board.black_pieces.keys():
                    active_piece_position = klicked_pos
            if event.type == pg.MOUSEBUTTONUP:
                if active_piece_position != None:
                    if active_piece_position in board.white_pieces.keys():
                        active_piece = board.white_pieces[active_piece_position]
                        board.white_pieces.pop(active_piece_position)
                        board.white_pieces[gui_to_logic_pos(event.pos[0], event.pos[1])] = active_piece
                        active_piece_position = None
                    else:
                        active_piece = board.black_pieces[active_piece_position]
                        board.black_pieces.pop(active_piece_position)
                        board.black_pieces[gui_to_logic_pos(event.pos[0], event.pos[1])] = active_piece
                        active_piece_position = None

        # RENDER YOUR GAME HERE
        screen.blit(board_image, (0, 100))

        for piece_position in board.white_pieces.keys():
            if piece_position != active_piece_position:
                screen.blit(piece_images[board.white_pieces[piece_position].player + board.white_pieces[piece_position].type], logic_to_gui_pos(piece_position[0], piece_position[1]))      
        
        for piece_position in board.black_pieces.keys():
            if piece_position != active_piece_position:
                screen.blit(piece_images[board.black_pieces[piece_position].player + board.black_pieces[piece_position].type], logic_to_gui_pos(piece_position[0], piece_position[1]))    
        
        if active_piece_position != None:
            if active_piece_position in board.white_pieces.keys():
                screen.blit(piece_images[board.white_pieces[active_piece_position].player + board.white_pieces[active_piece_position].type], (pg.mouse.get_pos()[0] - 37, pg.mouse.get_pos()[1] - 37))
            else:
                screen.blit(piece_images[board.black_pieces[active_piece_position].player + board.black_pieces[active_piece_position].type], (pg.mouse.get_pos()[0] - 37, pg.mouse.get_pos()[1] - 37))

        # flip() the display to put your work on screen
        pg.display.flip()

        clock.tick(20)

    pg.quit()