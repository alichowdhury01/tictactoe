# Inspired from https://github.com/Aprataksh/Tic-tac-toe/blob/master/tic_tac_toe.py 
# By user Aprataksh


print(
    "██     ██ ███████ ██       ██████  ██████  ███    ███ ███████     ████████  ██████      ████████ ██  ██████       ████████  █████   ██████       ████████  ██████  ███████\n"
    "██     ██ ██      ██      ██      ██    ██ ████  ████ ██             ██    ██    ██        ██    ██ ██               ██    ██   ██ ██               ██    ██    ██ ██\n"
    "██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████          ██    ██    ██        ██    ██ ██      █████    ██    ███████ ██      █████    ██    ██    ██ █████\n"
    "██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██             ██    ██    ██        ██    ██ ██               ██    ██   ██ ██               ██    ██    ██ ██\n"
    " ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████        ██     ██████         ██    ██  ██████          ██    ██   ██  ██████          ██     ██████  ███████")


class Tictactoe:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.move = 0
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
        # The try... except will try to see if there's any symbols 
        # From any users In the chosen cell. If no symbol it will add the 
        # Current player symbol. In the case where there is already Something, 
        # It will print that the cell is already taken and call
        # The player_one() method. If anything else then is entered that is 
        # Not in the list self.pos the except ValueError will print an error
        # This try to see any error and let me handle it
        # Taken from: https://www.w3schools.com/python/python_try_except.asp
        # By W3school
        try:
            self.user_position = int(input(f"Player {self.player_1}, please choose your position on the board: "))
            while self.user_position < 0 or self.user_position > 8:
                print("Please enter a NUMBER between 0 and 8")
                return self.player_one()
            if self.pos[self.user_position] != self.player_1 and self.pos[self.user_position] != self.player_2:
                self.pos[self.user_position] = self.player_1
                self.board()
                self.moves()
            else:
                print(self.taken)
                self.player_one()
        except ValueError:
            print("Please enter a NUMBER between 0 and 8")
            return self.player_one()

    def player_two(self):
        # The try... except will try to see if there's any symbols 
        # From any users In the chosen cell. If no symbol it will add the 
        # Current player symbol. In the case where there is already Something, 
        # It will print that cell is already taken and call 
        # The player_two() method. If anything else then is entered that is 
        # Not in the list self.pos the except ValueError will print an error
        # This will try to see any error and let me handle it
        # Taken from: https://www.w3schools.com/python/python_try_except.asp
        # By W3school
        try:
            self.user_position = int(input(f"Player {self.player_2}, please choose your position on the board: "))
            while self.user_position < 0 or self.user_position > 8:
                print("Please enter a NUMBER between 0 and 8")
                return self.player_two()
            if self.pos[self.user_position] != self.player_1 and self.pos[self.user_position] != self.player_2:
                self.pos[self.user_position] = self.player_2
                self.board()
                self.moves()
            else:
                print(self.taken)
                return self.player_two()
        except ValueError:
            print("Please enter a NUMBER between 0 and 8")
            self.player_two()

    def moves(self):
        # For each move played, the variable move
        # Will be incremented by one
        self.move += 1
        return self.move

    def check_win(self):

        # This code will verify each position of the winning combination 
        # Match with the player symbol. If there's a match, it will print
        # who won and call the method play_again()
        for symb in self.win_conditions:
            if self.pos[symb[0]] == self.pos[symb[1]] == self.pos[symb[2]] == self.player_1:
                print(f"Player {self.player_1} WIN!")
                self.play_again()
            if self.pos[symb[0]] == self.pos[symb[1]] == self.pos[symb[2]] == self.player_2:
                print(f"Player {self.player_2} WIN!")
                self.play_again()

    def check_draw(self):

        # Once the variable move reach 9,
        # It verifies if the opposite of the method
        # check_win, print it a draw and call the 
        # Method play_again()
        if self.move == 9:
            for symb in self.win_conditions:
                if self.pos[symb[0]] != self.pos[symb[1]] != self.pos[symb[2]] != self.player_1:
                    print("It's a TRAP! Kidding it's a DRAW!")
                    self.play_again()

    def play(self):
        while True:
            self.player_one()
            self.check_win()
            self.check_draw()
            self.player_two()
            self.check_win()
            self.check_draw()

    def run(self):
        self.board()
        self.play()

    def play_again(self):
        while True:
            question = input(f"Player {self.player_1} and {self.player_2}, would you like to play again?\n"
                             "Type y for YES or n for NO: ")
            if question == "y":
                self.pos = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                # If the player enter "y", it will reset the variable move to 0
                self.move = 0
                self.run()
            elif question == "n":
                print("See you next time!")
                quit()
            else:
                print("Invalid option!")


class Players:
    def __init__(self):

        self.player_1 = "X"
        self.player_2 = "O"

    def default_symb(self):
        return self.player_1, self.player_2

    def user_decision_symb(self):
        # The try... except, execute the code to see any if there's any error
        # And let me handle those errors
        # Taken from: https://www.w3schools.com/python/python_try_except.asp
        # By W3school
        try:
            self.users_selection = (input("1. Use default symbols X and O\n"
                                          "2. Choose your own symbols\n"
                                          "Please make a selection: "))
            self.users_selection = int(self.users_selection)
            while self.users_selection < 1 or self.users_selection > 2:
                print("Invalid option")
                self.users_selection = (input("1. Use default symbols X and O\n"
                                              "2. Choose your own symbols\n"
                                              "Please make a selection: "))
                self.users_selection = int(self.users_selection)
            if self.users_selection == 1:
                return self.default_symb()
            if self.users_selection == 2:
                self.player_a = str(input("First player please enter a symbol of your choice: "))
                self.player_b = str(input("Second player please enter a symbol of your choice: "))
                while self.player_a == self.player_b:
                    print("Second player, you can't enter the same symbol as the first player")
                    self.player_b = str(input("Second player please enter a symbol of your choice: "))
                return self.player_a.upper(), self.player_b.upper()
        except ValueError:
            print("invalid")
            self.user_decision_symb()


if __name__ == "__main__":
    players = Players()
    player_1, player_2 = players.user_decision_symb()
    game = Tictactoe(player_1, player_2)
    game.run()
