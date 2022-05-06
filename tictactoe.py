
# Inspired from https://github.com/Aprataksh/Tic-tac-toe/blob/master/tic_tac_toe.py 
# By user Aprataksh

from tabnanny import check


print("██     ██ ███████ ██       ██████  ██████  ███    ███ ███████     ████████  ██████      ████████ ██  ██████       ████████  █████   ██████       ████████  ██████  ███████\n"
      "██     ██ ██      ██      ██      ██    ██ ████  ████ ██             ██    ██    ██        ██    ██ ██               ██    ██   ██ ██               ██    ██    ██ ██\n"
      "██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████          ██    ██    ██        ██    ██ ██      █████    ██    ███████ ██      █████    ██    ██    ██ █████\n"
      "██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██             ██    ██    ██        ██    ██ ██               ██    ██   ██ ██               ██    ██    ██ ██\n"
      " ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████        ██     ██████         ██    ██  ██████          ██    ██   ██  ██████          ██     ██████  ███████")                                                                                                                                                                           
                                                                                                                                                                        

class Tictactoe:
    
    def __init__(self):
        self.pos = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.win_conditions = [[0, 1, 2], [3, 4, 5],
                               [6, 7, 8], [0, 4, 8], 
                               [2, 4, 6], [0, 3, 6], 
                               [1, 4, 7], [2, 5, 8]]
        self.taken = "Cell already taken"

    def board(self):
        self.surface = print(f"     |     |\n"
                        f"  {self.pos[0]}  |  {self.pos[1]}  |  {self.pos[2]}\n"
                        f'_____|_____|_____\n'
                        f"     |     |\n"
                        f"  {self.pos[3]}  |  {self.pos[4]}  |  {self.pos[5]}\n"
                        f'_____|_____|_____\n'
                        f"     |     |\n"
                        f"  {self.pos[6]}  |  {self.pos[7]}  |  {self.pos[8]}\n"
                        f"     |     |")
        return self.surface

    def player_x(self):
        # Taken from: https://www.w3schools.com/python/python_try_except.asp
        # By W3school
        try:
            user_position = int(input("Player X, please choose your position on the board: "))
            if self.pos[user_position] != "X" and self.pos[user_position] != "O":
                self.pos[user_position] = "X"
                self.board()
            else:
                print(self.taken)
                self.player_x()
        except ValueError:
            print("Please enter a NUMBER between 0 and 8")
            self.player_x()

    def player_o(self):
        # Taken from: https://www.w3schools.com/python/python_try_except.asp
        # By W3school
        try:
            user_position = int(input("Player O, please choose your position on the board: "))
            if self.pos[user_position] != "X" and self.pos[user_position] != "O":
                self.pos[user_position] = "O"
                self.board()
            else:
                print(self.taken)
                self.player_o()
        except ValueError:
            print("Please enter a NUMBER between 0 and 8")
            self.player_o()

    def check_win(self):
        for symb in self.win_conditions:
            if self.board[symb[0]] == self.board[symb[1]] == self.board[symb[2]] == "X":
                print("Player X WIN!")
                self.play_again()
            if self.board[symb[0]] == self.board[symb[1]] == self.board[symb[2]] == "O":
                print("Player O WIN!")
                self.play_again()
        

    def play(self):
        while True:
            self.player_x()
            self.check_win()
            self.player_o()
            self.check_win()
            
    def run(self):
        self.board()
        self.play()
    
    def play_again(self):
        while True:
            question = input("Loosing player, would you like to try your luck again?\n"
                             "Type y for YES or n for NO: ")
            if question == "y":
                self.pos = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                self.run()
            elif question == "n":
                print("See you next time!")
                quit()
            else:
                print("Invalid option!")

a = Tictactoe()
a.run()