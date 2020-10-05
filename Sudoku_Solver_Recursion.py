import string
import random
import numpy as np
from collections import Counter
#SODUKU SOLVER


#Brute force technique
#
# data P for the particular instance of the problem
#
# first (P): generate a first candidate solution for P.
# next (P, c): generate the next candidate for P after the current one c.
# valid (P, c): check whether candidate c is a solution for P.
# output (P, c): use the solution c of P as appropriate to the application.
#
# c ← first(P)
# while c ≠ Λ do
#     if valid(P,c) then
#         output(P, c)
#     c ← next(P, c)
# end while
#################################################################################
# Constraints
# 1-9 in column, row and box

#Approach - Brute force

# 1. Generate all boards --> Genereate each possible number in each empty box, e.g. 1-9.
# 2. Validate all boards
# 3. Return all valid boards
# E.g. one board can consist of only 5:s in the empty boxes.

#Approach - Backtracking

# 1. Generate number 1-9 in first empty box.
# 2. Check if the number is ok with the constraints.
# 3. If yes proceed to the next empty box in the row.
# 4. Start at step one again -->





def create_grid():

	a = np.array([[5 ,3 ,0  ,0 ,7 ,0  ,0 ,0 ,0],
				  [6 ,0 ,0  ,1 ,9 ,5  ,0 ,0 ,0],
				  [0 ,9 ,8  ,0 ,0 ,0  ,0 ,6 ,0],
				  [8 ,0 ,0  ,0 ,6 ,0  ,0 ,0 ,3],
				  [4 ,0 ,0  ,8 ,0 ,3  ,0 ,0 ,1],
				  [7 ,0 ,0  ,0 ,2 ,0  ,0 ,0 ,6],
				  [0 ,6 ,0  ,0 ,0 ,0  ,2 ,8 ,0],
				  [0 ,0 ,0  ,4 ,1 ,9  ,0 ,0 ,5],
				  [0 ,0 ,0  ,0 ,8 ,0  ,0 ,7 ,9]])


	# a = np.array([[0 ,0 ,0  ,0 ,0 ,0  ,0 ,8 ,6],
	# 			  [0 ,7 ,8  ,5 ,0 ,9  ,0 ,0 ,0],
	# 			  [0 ,1 ,0  ,0 ,2 ,0  ,0 ,4 ,9],
	# 			  [6 ,0 ,0  ,0 ,4 ,0  ,0 ,0 ,0],
	# 			  [0 ,0 ,0  ,0 ,0 ,1  ,0 ,0 ,5],
	# 			  [0 ,0 ,0  ,3 ,0 ,0  ,8 ,0 ,0],
	# 			  [0 ,0 ,0  ,6 ,0 ,3  ,0 ,0 ,0],
	# 			  [0 ,9 ,0  ,0 ,0 ,0  ,2 ,0 ,0],
	# 			  [0 ,0 ,0  ,4 ,0 ,0  ,0 ,0 ,0]])

	return a



def row_constraint(grid,row,col,n):

	#Number to check if possible in the row
	check_number = n
	grid_tmp = grid.copy()
	grid_tmp[row,col] = n

	current_row = grid_tmp[row,:].tolist()

	duplicate_list = [k for k,v in Counter(current_row).items() if v>1]


	return False if n in duplicate_list else True


def column_constraint(grid,row,col,n):
	# Number to check if possible in the row
	check_number = n
	grid_tmp = grid.copy()
	grid_tmp[row, col] = n

	current_col = grid_tmp[:, col].tolist()

	duplicate_list = [k for k, v in Counter(current_col).items() if v > 1 if k != 0]


	return False if n in duplicate_list else True

def box_constraint(grid,row,col,n):
	check_number = n
	grid_tmp = grid.copy()
	grid_tmp[row, col] = n

	# One box is a 3x3 "sub"-matrix

	#Locate in what box the "pointer" is at. E.g. in which box is row,col located at?
	# When that box is found, check for duplicates in the box.


	if row <= 2:
		row_low_limit = 0
		row_high_limit = 3
	elif row <= 5:
		row_low_limit = 3
		row_high_limit = 6
	else:
		row_low_limit = 6
		row_high_limit = 9

	if col <= 2:
		col_low_limit = 0
		col_high_limit = 3
	elif col <= 5:
		col_low_limit = 3
		col_high_limit = 6
	else:
		col_low_limit = 6
		col_high_limit = 9



	current_box = grid_tmp[row_low_limit:row_high_limit, col_low_limit:col_high_limit].reshape(-1).tolist()

	duplicate_list = [k for k, v in Counter(current_box).items() if v > 1 if k != 0]


	return False if n in duplicate_list else True



def solution():
	print(50*"#")
	print(grid)
	print(50*"_")
	print("New sol iter")
	for row in grid_index:
		for col in grid_index:
			print("row,col",row,col)
			if grid[row,col] == 0:
				for n in numbers:
					if row_constraint(grid,row,col,n):
						if column_constraint(grid,row,col,n):
							if box_constraint(grid,row,col,n):
								print("The number placed: ",n)
								grid[row,col] = n
								# print("Pre")
								solution()
								# print("After")
								print("SETTING row,col: ",row,col," ---- to number 0")
								#Setting the grid at row,col to zero because we ended up with the wrong solution.
								grid[row,col] = 0
				return
	# print(grid)


def header():
	global grid,grid_index,numbers

	grid = create_grid()
	grid_index = np.arange(0,9)
	numbers = np.arange(1,10)

	solution()





if __name__ == '__main__':
	header()



