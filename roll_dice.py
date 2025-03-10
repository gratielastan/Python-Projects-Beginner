#simulate rolling a six-sided dice using the random module.

import random  # to import the module to use it
# this will allow us to us its functions in our program

roll = random.randint(1,6) # this function will return a random number between 1 and 6
#print("The computer rolled a "+ str(roll)) # don't forget to convert the int to a string to concatenate it

guess = int(input("Guess the dice roll:\n")) # convert the input to an INT so we can compare GUESS to ROLL
if guess == roll:
    print("Correct! They rolled a " + str(roll))
else:
    print("Wrong! They rolled a " + str(roll))
