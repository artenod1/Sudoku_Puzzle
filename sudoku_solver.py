import numpy as np
from get_rcs import *
from get_zero_index import get_zero_index
from check_position import check_position


def solve(puzzle):
    find_zero = get_zero_index(puzzle)
    if not find_zero:
        # print(puzzle)
        return True

    else:
        row = find_zero[0]
        column = find_zero[1]
        for num in range(1, 10):
            if check_position(puzzle, row, column, num):
                puzzle[row][column] = num
                print(puzzle)

                if solve(puzzle):
                    return True

                puzzle[row][column] = 0
