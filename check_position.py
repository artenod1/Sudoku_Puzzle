import numpy as np
from get_rcs import get_row
from get_rcs import get_column
from get_rcs import get_square


def check_position(puzzle, r, c, num):

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
