# A program that similates rolling a dice

#TODO:
#Have the computer choose a random number between one and six
#Display the number
#Have the option to quit the program
#Extra feature: choose different types of dice

import random

PLAY = True


print("Roll the dice?")


while PLAY:

    response = input()

    if response.lower() == "yes":
        ROLL = random.randint(1,6)
        print("You rolled a " + str(ROLL))
    elif response.lower() == "quit" or "no":
        PLAY = False
    else:
        print("Please type 'yes', 'no', or 'quit.'")

    print("Do you want to roll again?")

print("Thanks for playing!")