import cellpylib as cpl
import numpy as np


def fill_board(board: np.array, vals: list, x0: int, y0: int, w: int, h: int) -> np.array:
    for i, x in enumerate(range(x0, x0 + w)):
        for j, y in enumerate(range(y0, y0 + h)):
            board[:, x, y] = vals[i*w + j]
    return board
