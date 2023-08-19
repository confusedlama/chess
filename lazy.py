# pieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
# for i in range(1, 9):
#     print(f"({i}, 1): \"{pieces[i-1]}\", ")

import cv2
from os import listdir
from os.path import join
import numpy as np

# png_paths = [png for png in listdir("pieces copy")]

# for png_path in png_paths:
#     png = cv2.imread(join("pieces copy", png_path), cv2.IMREAD_UNCHANGED)

#     downscaled = cv2.resize(png, [75, 75])

#     cv2.imwrite(join("pieces", png_path), downscaled)

# board_background = np.zeros((75*8, 75*8, 3))

# black = (197, 143, 54)
# white = (249, 242, 232)

# for row in range(75*8):
#     for column in range(75*8):
#         if row//75 % 2 == column//75 % 2:
#             board_background[row][column][0] = white[0]
#             board_background[row][column][1] = white[1]
#             board_background[row][column][2] = white[2]
#         else:
#             board_background[row][column][0] = black[0]
#             board_background[row][column][1] = black[1]
#             board_background[row][column][2] = black[2]

# cv2.imwrite("board.png", board_background)