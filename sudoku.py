import numpy as np
from get_rcs import *
from get_zero_index import get_zero_index
from check_position import check_position
from sudoku_solver import solve


row1 = np.array([7, 9, 0, 0, 0, 0, 3, 0, 0])
row2 = np.array([0, 0, 0, 0, 0, 6, 9, 0, 0])
row3 = np.array([8, 0, 0, 0, 3, 0, 0, 7, 6])
row4 = np.array([0, 0, 0, 0, 0, 5, 0, 0, 2])
row5 = np.array([0, 0, 5, 4, 1, 8, 7, 0, 0])
row6 = np.array([4, 0, 0, 7, 0, 0, 0, 0, 0])
row7 = np.array([6, 1, 0, 0, 9, 0, 0, 0, 8])
row8 = np.array([0, 0, 2, 3, 0, 0, 0, 0, 0])
row9 = np.array([0, 0, 9, 0, 0, 0, 0, 5, 4])


puzzle = np.array([row1, row2, row3, row4, row5, row6, row7, row8, row9])

print(solve(puzzle))





# Ask user to imput a row at a time, with zeros for blanks.

print("Input numbers 1-9 for your sudoku puzzle without spaces or commas. Enter 0 for blank spaces.")

r1 = input("Row 1: ")
r2 = input("Row 2: ")
r3 = input("Row 3: ")
r4 = input("Row 4: ")
r5 = input("Row 5: ")
r6 = input("Row 6: ")
r7 = input("Row 7: ")
r8 = input("Row 8: ")
r9 = input("Row 9: ")

# take numbers given, separate into 9 lists.

list_r1 = []
for num in r1:
    list_r1.append(int(num))


list_r2 = []
for num in r2:
    list_r2.append(int(num))

list_r3 = []
for num in r3:
    list_r3.append(int(num))

list_r4 = []
for num in r4:
    list_r4.append(int(num))

list_r5 = []
for num in r5:
    list_r5.append(int(num))

list_r6 = []
for num in r6:
    list_r6.append(int(num))

list_r7 = []
for num in r7:
    list_r7.append(int(num))

list_r8 = []
for num in r8:
    list_r8.append(int(num))

list_r9 = []
for num in r9:
    list_r9.append(int(num))

puzzle = np.array([list_r1, list_r2, list_r3, list_r4, list_r5, list_r6, list_r7, list_r8, list_r9])

print(puzzle)



solve(puzzle)


