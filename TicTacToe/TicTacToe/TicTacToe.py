class TicTacToe:
    # Sets the original playground
    playground = ["| 1 | 2 | 3 |", "|---|---|---|", "| 4 | 5 | 6 |", "|---|---|---|", "| 7 | 8 | 9 |"]
    tempplayground = []
    turn = 0
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
        print("Player " + str(self.p1) + " it is your turn!")
        print("What field do you choose?")

        playerinput = input("Field: ")
        print()
        win = self.CheckInput(playerinput, self.p1)
        return win
    def TurnPlayerTwo(self):
        print("Player " + str(self.p2) + " it is your turn!")
        print("What field do you choose?")

        playerinput = input("Field: ")
        print()
        win = self.CheckInput(playerinput, self.p2)
        return win
       
    # Checks player inputs
    def CheckInput(self, input, player):
        field = input
        self.PrintPlayground(field, player)
        self.turn += 1
        if self.turn >= 5:
            win = self.CheckWin(player)
            return win


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

    # Checks if someone has won
    def CheckWin(self, player):
        row = 0
        win = 0
        # horizontally
        for i in range(0, 5, 2):
            for i in range(2, 11, 4):
                if self.playground[row][i] == player:
                    win += 1
                else:
                    print("No")
                    win = 0
            if win == 3:
                print("Player " + str(player) + " has won the game!")
                return True
            row += 2
        # vertical
        row = 0
        column = 0
        win = 0

# Start game
print("-- Welcome to TicTacToe --")
while True:
    print("This is the playground")
    game = TicTacToe()
    game.PrintExample()
    print("")

    # Play for 5 rounds
    for i in range(0, 5):
        if game.TurnPlayerOne():
            break
        if game.TurnPlayerTwo():
            break
    print("--------------")
    print("---Gameover---")
    print("--------------")
    # Ask to leave the game
    print("Do you want to quit? (write 'quit' to leave)")
    playerinput = input()
    if playerinput == "quit":
       break