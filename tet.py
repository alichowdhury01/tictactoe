"""    def players_choices(self):
        self.users_selection = int(input("1. Use default symbols X and O\n"
                                     "2. Choose your own symbols\n"
                                     "Please make a selection: "))
        if self.users_selection == 1:
            return self.player_1, self.player_2
        if self.users_selection == 2:
            self.player_a = str(input("First player please enter a symbol of your choice: "))
            self.player_b = str(input("Second player please enter a symbol of your choice: "))
            if self.player_2 == self.player_1:
                print("Second player, you can't enter the same symbol as the first player")
            return self.player_a, self.player_b"""

class Sdd:
    def __init__(self):
        self.j="l"
        self.jj="gf"

    def bb(self):
        self.hgfr = (input("hqfjij: "))
        if int(self.hgfr) == 1:
                return print(self.j), print(self.jj)
        elif int(self.hgfr) == 2:
                self.j = input("hhg:")
                self.jj = input("ffssef:")
                return print(self.j, self.jj)
        else:
            print(";;;;")
            self.jj = input("ffssef:")
            return print(self.jj, self.j)


            


a=Sdd()
a.bb()