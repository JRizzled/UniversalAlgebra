

## Build database of solved sudokus
## Figure out algebra and characteristics of sudokus and 10 x 10 matrixes of nums of 0-9 unique squares, rows, cols
## If you get commutive property, that would be interesting
## Create sudoku database in xml UA form
## Take solved sudokus or generate them, or output that creates algebras that are binary that can be stored or investigated in UA calc
## Code Would be populating
## Find 

sud_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
sud_squareNum = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6:2, 7:2, 8:2}

class board_member:
	def __init__(self, row, col, square, value=None):

		self.row = row
		self.col = col
		self.square = square
		self.value = value
	def __str__(self):
		return self.value
class board:
	row_dict = {0:{},1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{}}
	col_dict = {0:{},1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{}}
	square_dict = {0:{},1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{}}

	def __init__(self):
		self.board_arr = [[],[],[],[],[],[],[],[],[]]
		for i in range(9):
			for j in range(9):
				self.board_arr[i].append(board_member(i, j, (3* sud_squareNum[i])+sud_squareNum[j], ' '))
	def print_board(self):
		for i in range(9):
			for j in range(9):
				if (j == 0):
					print(' ',end='')
				print(self.board_arr[i][j], end='')
				if j >= 0 and j < 8:
					if j in [2,5, 8]:
						print(" ║ ",end='')
					else:
						print(" | ",end='')
			print()
			if i < 8:

				if i in [2,5, 8]:
					print("═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══ ")
				else:
					print("―――+―――+―――╬―――+―――+―――╬―――+―――+―――  ")
def main():
	bb = board()
	bb.print_board()


if __name__ == '__main__':
	main()