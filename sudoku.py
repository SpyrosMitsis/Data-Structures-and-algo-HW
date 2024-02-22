import pandas as pd


dataset = pd.read_csv("sudoku.csv")

sudoku_board = [[None for _ in range(9)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        sudoku_board[i][j] = dataset.iloc[i, 0][j]

for i in sudoku_board:
    print(i)