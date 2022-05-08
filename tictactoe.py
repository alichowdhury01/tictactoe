
# Inspired from https://github.com/Aprataksh/Tic-tac-toe/blob/master/tic_tac_toe.py 
# By user Aprataksh

from tabnanny import check

from self import self


print("██     ██ ███████ ██       ██████  ██████  ███    ███ ███████     ████████  ██████      ████████ ██  ██████       ████████  █████   ██████       ████████  ██████  ███████\n"
      "██     ██ ██      ██      ██      ██    ██ ████  ████ ██             ██    ██    ██        ██    ██ ██               ██    ██   ██ ██               ██    ██    ██ ██\n"
      "██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████          ██    ██    ██        ██    ██ ██      █████    ██    ███████ ██      █████    ██    ██    ██ █████\n"
      "██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██             ██    ██    ██        ██    ██ ██               ██    ██   ██ ██               ██    ██    ██ ██\n"
      " ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████        ██     ██████         ██    ██  ██████          ██    ██   ██  ██████          ██     ██████  ███████")                                                                                                                                                                           
                                                                                                                                                                        

class Tictactoe:
    
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
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

    def player_one(self):
        # Taken from: https://www.w3schools.com/python/python_try_except.asp
        # By W3school
        try:
            user_position = int(input(f"Player {self.player_1}, please choose your position on the board: "))
            if self.pos[user_position] != self.player_1 and self.pos[user_position] != self.player_2:
                self.pos[user_position] = self.player_1
                self.board()
            else:
                print(self.taken)
                self.player_one()
        except ValueError:
            print("Please enter a NUMBER between 0 and 8")

    def player_two(self):
        # Taken from: https://www.w3schools.com/python/python_try_except.asp
        # By W3school
        try:
            user_position = int(input(f"Player {self.player_2}, please choose your position on the board: "))
            if self.pos[user_position] != self.player_1 and self.pos[user_position] != self.player_2:
                self.pos[user_position] = self.player_2
                self.board()
            else:
                print(self.taken)
                self.player_two()
        except ValueError:
            print("Please enter a NUMBER between 0 and 8")
            self.player_two()

    def check_win(self):
        for symb in self.win_conditions:
            if self.pos[symb[0]] == self.pos[symb[1]] == self.pos[symb[2]] == self.player_1:
                print(f"Player {self.player_1} WIN!")
                self.play_again()
            if self.pos[symb[0]] == self.pos[symb[1]] == self.pos[symb[2]] == self.player_2:
                print(f"Player {self.player_2} WIN!")
                self.play_again()

    def play(self):
        while True:
            self.player_one()
            self.check_win()
            self.player_two()
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

    def rematch(self):
        while True:
            question = input(f"Player {self.player_1} and {self.player_2}, would like a rematch ?\n"
                             f"Type y for YES or n for NO: ")
            if question == "y":
                self.pos = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                self.run()
            elif question == "n":
                print("See you next time!")
                quit()
            else:
                print("Invalid option!")

class Players:
    def __init__(self):

        self.player_1 = "X"
        self.player_2= "O"

    def default_symb(self):
        return self.player_1, self.player_2

    def user_decision_symb(self):
        self.users_selection = int(input("1. Use default symbols X and O\n"
                                     "2. Choose your own symbols\n"
                                     "Please make a selection: "))
        while int(self.users_selection) < 1 or int(self.users_selection) > 2:
            print("Invalid option")
            self.users_selection = int(input("1. Use default symbols X and O\n"
                                        "2. Choose your own symbols\n"
                                        "Please make a selection: "))
        if self.users_selection == 1:
                return self.default_symb()
        if self.users_selection == 2:
                self.player_a = str(input("First player please enter a symbol of your choice: "))
                self.player_b = str(input("Second player please enter a symbol of your choice: "))
                while self.player_a == self.player_b:
                    print("Second player, you can't enter the same symbol as the first player")
                    self.player_b = str(input("Second player please enter a symbol of your choice: "))
                return self. player_a, self.player_b


if __name__ == "__main__":
    players = Players()
    player_1, player_2 = players.user_decision_symb()
    game = Tictactoe(player_1, player_2)
    game.run()

