class TicTacToe:
    # Sets the original playground
    playground = ["| f1 | f2 | f3 |", "|---|---|---|", "| f4 | f5 | f6 |", "|---|---|---|", "| f7 | f8 | f9 |"]
    p1 = "X"
    p2 = "O"

    # First playground output
    def PrintExample(self):
        print("--TicTacToe--")
        print(self.playground[0].format(f1 = 1, f2 = 2, f3 = 3))
        print(self.playground[1])
        print(self.playground[2].format(f4 = 4, f5 = 5, f6 = 6))
        print(self.playground[3])
        print(self.playground[4].format(f7 = 7, f8 = 8, f9 = 9))

    # Player turns
    def TurnPlayerOne(self):
        print("Player 1 it is your turn!")
        print("What field do you choose?")

        playerinput = input("Field: ")
        print()
        self.CheckInput(playerinput, self.p1)
    
    def TurnPlayerTwo(self):
        print("Player 2 it is your turn!")
        print("What field do you choose?")

        playerinput = input("Field: ")
        print()
        self.CheckInput(playerinput, self.p2)
       
    # Checks player inputs
    def CheckInput(self, input, player):
        field = "f" + input
        self.PrintPlayground(field, player)

    # Prints changed playground
    def PrintPlayground(self, field, player):
        for str in self.playground:
            if field in str:
                newstr = str.replace(field, player)
                print(newstr)
            else:
                print(str)
                


# Start game
print("-- Welcome to TicTacToe --")
print("This is the playground")
game = TicTacToe()
game.PrintExample()
print("")

while True:
    game.TurnPlayerOne()
    game.TurnPlayerTwo()
