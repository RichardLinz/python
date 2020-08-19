import random

# Function random number between 1-100
def createRandomNumber():
    num = random.randrange(1,100)
    return num

def game():
    counter = 1
    rnum = createRandomNumber()
    while True:
        userinput = input("What is your guess: ")

        # Check the input
        try:
            if userinput == "quit": # When input is "quit"
                break
            elif int(userinput) > rnum: # When input is bigger
                print("Your number is bigger.")
            elif int(userinput) < rnum: # When input is smaller
                print("Your number is smaller.")
            elif int(userinput) == rnum: # When input is right
                print("You guessed right, the number was: " + str(rnum))
                print("You needed " + str(counter) + " tries.")
                # Ask to continue game
                print("Do you want to continue? (write quit to leave)")
                userinput = input()
                if userinput == "quit": # When input is "quit"
                    print("quitting game")
                    break
                else:
                    counter = 0
                    rnum = createRandomNumber()
            # Rise counter
            counter += 1
        except:
            print("Your input is not valid.")
            continue

# Starting game
print("++ Guess the random number ++")
game()
