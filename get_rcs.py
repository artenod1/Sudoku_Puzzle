import numpy as np


def get_row(puzzle, row):
    """Returns column for given index"""
    return puzzle[row]


def get_column(puzzle, column):
    """Returns column for given index"""
    return puzzle[0:9, column]


def get_square(puzzle, row, column):
    """Returns 3x3 array for given row and column index"""
    if row in range(3):
        if column in range(3):
            x = puzzle[0][0:3]
            y = puzzle[1][0:3]
            z = puzzle[2][0:3]
            return np.hstack((x, y, z))
        elif column in range(3, 6):
            x = puzzle[0][3:6]
            y = puzzle[1][3:6]
            z = puzzle[2][3:6]
            return np.hstack((x, y, z))
        else:
            x = puzzle[0][6::]
            y = puzzle[1][6::]
            z = puzzle[2][6::]
            return np.hstack((x, y, z))
    elif row in range(3, 6):
        if column in range(3):
            x = puzzle[3][0:3]
            y = puzzle[4][0:3]
            z = puzzle[5][0:3]
            return np.hstack((x, y, z))
        elif column in range(3, 6):
            x = puzzle[3][3:6]
            y = puzzle[4][3:6]
            z = puzzle[5][3:6]
            return np.hstack((x, y, z))
        else:
            x = puzzle[3][6::]
            y = puzzle[4][6::]
            z = puzzle[5][6::]
            return np.hstack((x, y, z))
    else:
        if column in range(3):
            x = puzzle[6][0:3]
            y = puzzle[7][0:3]
            z = puzzle[8][0:3]
            return np.hstack((x, y, z))
        elif column in range(3, 6):
            x = puzzle[6][3:6]
            y = puzzle[7][3:6]
            z = puzzle[8][3:6]
            return np.hstack((x, y, z))
        else:
            x = puzzle[6][6::]
            y = puzzle[7][6::]
            z = puzzle[8][6::]
            return np.hstack((x, y, z))
