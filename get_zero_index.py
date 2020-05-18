import numpy as np


def get_zero_index(puzzle):
    """
    finds the row and column index (i,j) for a zero (blank) space in the puzzle.
    """

    i = 0
    for row in puzzle:

        j = 0
        for num in row:
            if num == 0:
                return (i, j)
            else:
                j += 1
        i += 1

    return None
