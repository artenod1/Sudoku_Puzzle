import numpy as np
from get_rcs import *
from get_zero_index import get_zero_index
from check_position import check_position


def solve(puzzle):
	"""
	Main function that solves input puzzle.
	"""
    
	# Use a backtracking recursion algorithm

	# Base case (no zeros in puzzle)
	find_zero = get_zero_index(puzzle)
	if not find_zero:
        # print(puzzle)
		return True

    # Recursion
	else:
	    row = find_zero[0]
	    column = find_zero[1]
	    for num in range(1, 10):
	        if check_position(puzzle, row, column, num):
	            puzzle[row][column] = num
	            # print puzzle so each step in process is printed
	            print(puzzle)

	            if solve(puzzle):
	                return True

	            # Number did not work, reset to zero.
	            puzzle[row][column] = 0
