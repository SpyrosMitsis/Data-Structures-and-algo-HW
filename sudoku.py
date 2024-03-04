import pandas as pd


# dataset = pd.read_csv("sudoku.csv")

# sudoku_board = [[None for _ in range(9)] for _ in range(9)]

# for i in range(9):
#     for j in range(9):
#         sudoku_board[i][j] = dataset.iloc[i, 0][j]

# for i in sudoku_board:
#     print(i)


def print_board(board):
    for i in board:
        print(i)

def is_valid_move(board, row, col, number):

    corner_row = row - row % 3
    corner_col= col - col % 3

    for i in range(9):
        if board[row][i] == number:
            return False
        if board[i][col] == number:
            return False

        
    for i in range(3):
        for j in range(3):
            if board[corner_row + i][corner_col + j] == number:
                return False
    return True
        
    
def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for n in range(1, 10):
                    if is_valid_move(board, i, j, n):
                        board[i][j] = n
                        solve(board)
                        board[i][j] = 0
                return 
    print_board(board)
    print("\nAlternate solution\n")
    return 



sudoku_board = [[2, 0, 5, 3, 0, 8, 4, 0, 9],
                 [0, 7, 0, 0, 0, 0, 0, 5, 0],
                 [0, 0, 4, 0, 0, 0, 6, 0, 7],
                 [5, 0, 0, 0, 4, 0, 0, 0, 2],
                 [0, 0, 0, 5, 0, 7, 0, 0, 0],
                 [6, 0, 0, 0, 3, 0, 0, 0, 8],
                 [4, 0, 6, 0, 0, 0, 8, 0, 1],
                 [0, 2, 0, 0, 0, 0, 0, 6, 0],
                 [8, 0, 1, 2, 0, 9, 7, 0, 4]]

                 

solve(sudoku_board)
