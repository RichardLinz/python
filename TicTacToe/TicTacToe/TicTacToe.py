class TicTacToe:
    # Sets the original playground
    playground = ["| 1 | 2 | 3 |", "|---|---|---|", "| 4 | 5 | 6 |", "|---|---|---|", "| 7 | 8 | 9 |"]
    tempplayground = []
    p1 = "X"
    p2 = "O"

    # First playground output
    def PrintExample(self):
        print("--TicTacToe--")
        print(self.playground[0])
        print(self.playground[1])
        print(self.playground[2])
        print(self.playground[3])
        print(self.playground[4])

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
        field = input
        self.PrintPlayground(field, player)

    # Prints changed playground
    def PrintPlayground(self, field, player):
        self.tempplayground = []
        for str in self.playground:
            if field in str:
                str = str.replace(field, player)
                print(str)
                self.tempplayground.append(str)
            else:
                self.tempplayground.append(str)
                print(str)
        self.playground = self.tempplayground

# Start game
print("-- Welcome to TicTacToe --")
print("This is the playground")
game = TicTacToe()
game.PrintExample()
print("")

while True:
    game.TurnPlayerOne()
    game.TurnPlayerTwo()
