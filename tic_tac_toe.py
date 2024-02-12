import time

class TicTacToe:
    def __init__(self) -> None:
        self.board = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]


    ''' 
    Display the board
    '''
    def display_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end=' ')
            print()

    '''
    Human player makes a move
    :param player: X or O
    :return: row, col
    '''
    def human_play(self, player):

        while True:

            row = int(input("Row: "))
            col = int(input("Col: "))

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Wrong row or col")
            elif self.board[row][col] == '-':
                self.board[row][col] = player
                return row, col
            else:
                print("Error, position is occupied")



    '''.
    Check if there is a winner
    :param player: X or O
    :return: True or False
    '''
    def is_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                return True

        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False
    
    '''
    Check if the board is full
    :return: True or False
    '''
    def is_board_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    return False
        return True

    '''
    Evaluate the board
    :return: 1 if O wins, -1 if X wins, 0 if it's a tie
    '''
    def evaluate(self):

        if self.is_winner("O"):
            return 1
        elif self.is_winner("X"):
            return -1
        elif self.is_board_full():
            return 0
        else:
            return None
            

    '''
    Minimax algorithm
    :param depth: depth of the tree
    :param alpha: alpha value
    :param beta: beta value
    :param max_player: True if it's the max player, False if it's the min player
    :return:
    '''
    def minimax(self, depth, alpha, beta, max_player):

        score = self.evaluate()

        if score is not None:
            return score
        
        if max_player:
            max_value = -2
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '-':
                        self.board[i][j] = 'O'
                        eval = self.minimax(depth + 1, alpha, beta, False)
                        self.board[i][j] = '-'
                        max_value = max(max_value, eval)
                        alpha = max(alpha, eval)

                        if beta <= alpha:
                            break

            return max_value

        else:
            min_value = 2
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '-':
                        self.board[i][j] = 'X'
                        eval = self.minimax(depth + 1,alpha, beta, True)
                        self.board[i][j] = "-"
                        min_value = min(min_value, eval)
                        beta = min(beta, eval)
                        
                        if beta <= alpha:
                            break
            return min_value



    '''
    Find the best move
    :return: row, col
    '''
    def best_move(self):
        
        start_time = time.time()

        best_score = float('-inf')
        best_move = None
        
        alpha = float('-inf')
        beta = float('inf')

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "-":
                    self.board[i][j] = "O"  
                    move_score = self.minimax(0,alpha, beta, False)
                    self.board[i][j] = '-'

                    if move_score > best_score:
                        best_move = (i, j)
                        best_score = move_score

                
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Minimax execution time: {execution_time:.6f} seconds")

        return best_move


    '''
    Computer player makes a move
    '''
    def ai_play(self):
        
        row, col = self.best_move()
        self.board[row][col] = 'O'

    ''' 
    Play the game
    '''
    def play_game(self):
        
        while True:
            print("Player move")
            print("-------")
            self.display_board()
            row, col = self.human_play("X")

            self.display_board()

            if self.is_winner("X"):
                print("You won")
                break
            if self.is_board_full():
                print("It's a tie")
                break

            self.ai_play()
            print("-------")

            if self.is_winner("O"):
                print("You lost")
                break
            if self.is_board_full():
                print("It's a tie")
                break


game = TicTacToe()
game.play_game()
