import sys
import os
print(os.getcwd())


def read_sudoku(filename):
    with open(filename, 'r') as f:
        board = [list(map(int, line.split())) for line in f]
    return board
print(read_sudoku('input.txt'))
def write_sudoku(filename, board):
    with open(filename, 'w') as f:
        for row in board:
            f.write(' '.join(map(str, row)) + '\n')

def is_valid_step(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board, row=0, col=0):
    if row == 9:
        return True
    if col == 9:
        return solve_sudoku(board, row+1, 0)
    if board[row][col] != 0:
        return solve_sudoku(board, row, col+1)
    for num in range(1, 10):
        if is_valid_step(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board, row, col+1):
                return True
    board[row][col] = 0
    return False

def main():
    board = read_sudoku('input.txt')
    if solve_sudoku(board):
        write_sudoku('output.txt', board)
    else:
        print('Impossible')
        sys.exit(1)

if __name__ == '__main__':
    main()
