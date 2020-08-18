import random

# Function random number between 1-100
def createRandomNumber():
    num = random.randrange(1,100)
    return num

def game():
    rnum = createRandomNumber()
    while True:
        userinput = input("What is your guess: ")

        # Check the input
        try:
            if int(userinput) > rnum:
                print("Your number is bigger.")
            elif int(userinput) < rnum:
                print("Your number is smaller.")
            elif int(userinput) == rnum: # When input is right
                print("You guessed right, the number was: " + str(rnum))
                # Ask to continue game
                print("Do you want to continue? (write quit to leave)")
                userinput = input()
                if userinput == "quit":
                    print("quitting game")
                    break
                else:
                    rnum = createRandomNumber()
            elif userinput == "quit":
                break
        except:
            print("Your input is not valid")
            continue

# Starting game
print("++ Guess the random number ++")
game()
