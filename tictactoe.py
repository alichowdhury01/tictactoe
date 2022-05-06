
# Inspired from https://github.com/Aprataksh/Tic-tac-toe/blob/master/tic_tac_toe.py 
# By user Aprataksh

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
        self.moves = 0
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
        try:
            user_position = int(input("Player X, please choose your position on the board: "))
            if self.pos[user_position] != "X" and self.pos[user_position] != "O":
                self.pos[user_position] = "X"
                self.board()
                self.moves +=1
            else:
                print(self.taken)
                self.player_x()
            self.check_win()
        except ValueError:
            print("Please enter a NUMBER between 0 and 8")
            self.player_x()

    def player_o(self):
        try:
            user_position = int(input("Player O, please choose your position on the board: "))
            if self.pos[user_position] != "X" and self.pos[user_position] != "O":
                self.pos[user_position] = "O"
                self.board()
                self.moves +=1
            else:
                print(self.taken)
                self.player_o()
            self.check_win()

        except ValueError:
            print("Please enter a NUMBER between 0 and 8")
            self.player_o()

    def check_win(self):
        for i in self.win_conditions:
            if all(j in self.pos for j in i):
                return True
            else:
                False
        

    def play(self):
        while True:
            self.player_x()
            self.player_o()

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