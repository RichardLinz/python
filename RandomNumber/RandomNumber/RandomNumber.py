import random
# Function random number between 1-100
def createRandomNumber():
    num = random.randrange(1,100)
    return num

# ----- Console output ------ #
print("++ Guess the random number ++")
userinput = input("What is your guess: ")
rnum = createRandomNumber()
# --------------------------- #

# Check the input
if int(userinput) == rnum:
    print("Congratulations you guessed right in the first try!!!")
else:
    # Loop while input is wrong
    while int(userinput) != rnum:
        if int(userinput) > rnum:
            print("Your number is bigger.")
        elif int(userinput) < rnum:
            print("Your number is smaller.")
        else:
            print("Your input is not valid.")

        userinput = input("Your next guess: ")
    # When input is right
    print("You guessed right, the number was: " + str(rnum))