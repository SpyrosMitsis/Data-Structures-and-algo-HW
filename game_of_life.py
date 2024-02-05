import random
import os
import time



class Game_of_life:

    def __init__(self, board_scale):
        self.board_scale = board_scale
        self.board = [[]]
        self.updated_board = [[" " for _ in range(board_scale)] for _ in range(board_scale)]


    def __str__(self):
        result = ""
        for row in self.board:
            result += ' '.join(row) + '\n'
        return result

    def board_maker(self):
        self.board = [[" " for _ in range(self.board_scale)] for _ in range(self.board_scale)]
        return self

    def place_cell(self):
        row  = int(input("Enter the row on the cell\n> "))
        col = int(input("Enter the collumn on the cell\n> "))

        self.board[row][col] = "X"
        return self

    def place_cell_auto(self, row, col):

        self.board[row][col] = "X"
        return self




    def random_board(self, n_of_cells):
        for i in range (n_of_cells):
            row = random.randint(0, self.board_scale - 1)
            col = random.randint(0, self.board_scale - 1)
            self.board[row][col] = "X"

        return self


    def neighbor_counter(self, row, col):

            count = 0 

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= row + i < self.board_scale and 0 <= col + j < self.board_scale:
                        if not (i == 0 and j == 0) and self.board[row + i][col + j] == 'X':
                            count += 1
            return count



        

    def next_board(self, row, col):
        cell = self.board[row][col]
        counter = self.neighbor_counter(row, col)

        if cell == " " and counter == 3:
            self.updated_board[row][col] = "X"
        elif cell == "X" and (counter < 2 or counter > 3):
            self.updated_board[row][col] = " "
        else:
            self.updated_board[row][col] = cell 








if __name__ == "__main__":
    game = Game_of_life(50)
    game.board_maker()
    game.random_board(300)
    #game.place_cell_auto(1, 1)
    #game.place_cell_auto(2, 1)
    #game.place_cell_auto(3, 1)

    for _ in range(100):

        os.system('cls')
        print(game)
        for i in range(game.board_scale):
            for j in range(game.board_scale):
                game.next_board(i, j)

        game.board = [row[:] for row in game.updated_board]
        time.sleep(0.5) 
        print(game)
