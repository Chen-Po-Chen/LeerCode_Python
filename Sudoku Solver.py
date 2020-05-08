board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

def solveSudoku(board):
	status = find_block_without_num(board)
	step = 0
	while status:
		for i in range(9):
			for j in range(9):
				for guess in range(9):
					row_status = check_row(board, guess, i, j)
					col_status = check_col(board, guess, i, j)
					grid_status = check_grid(board, guess, i, j)
					
				if row_status == True and col_status == True and grid_status == True:
					board[i][j] = str(guess)
		status = find_block_without_num(board)
		if step%500==0:
			for i in range(9):
				print(board[i])
			print("\n\n\n")
		step += 1
                
            
def find_block_without_num(board):
	for i in range(9):
		for j in range(9):
			if board[i][j] == ".":
				return True
	return False

def check_row(board, num, raw, col):
	if str(num) not in board[raw][:]:
		return True
	else:
		return False

def check_col(board, num, raw, col):
	if str(num) not in board[:][col]:
		return True
	else:
		return False

def check_grid(board, num, raw, col):
	grid_x = col//3
	grid_y = raw//3
	if str(num) not in board[grid_y*3:grid_y*3+3][grid_x*3:grid_x*3+3]:
		return True
	else:
		return False

solveSudoku(board)