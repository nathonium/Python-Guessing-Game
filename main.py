# Guessing game in Python.

# Imports every function from random.
from random import *

# Title
print("Guessing Game\n")

# Defines a number and an amount of tries.
number = randint(1, 10)
tries = 5

# Gives the player however many tries were defined, in this case 5.
for i in range(tries):
    # Let the player guess a number
    guess = int(input("Guess: "))

    # Check if the player's guess is equal to the defined number. If it is, give a win message and take
    # player input to end the game. If it isn't, have the player keep guessing until tries run out.
    if guess == number:
        print("You Win!")
        
        input()
    else:
        print("Guess again!")