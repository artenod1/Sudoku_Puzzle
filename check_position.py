import numpy as np
from get_rcs import get_row
from get_rcs import get_column
from get_rcs import get_square


def check_position(puzzle, r, c, num):

    """
    Puzzle, row, column, and a number are parameters. Function calls get_row,
    get_col, and get_square to get all numbers in row, column, and square. If the
    num input is in one of those lists, return False.
    """
    row = get_row(puzzle, r).tolist()
    column = get_column(puzzle, c).tolist()
    square = get_square(puzzle, r, c).tolist()

    total = []
    total.extend(row)
    total.extend(column)
    total.extend(square)

    if num in total:
        return False
    else:
        return True
