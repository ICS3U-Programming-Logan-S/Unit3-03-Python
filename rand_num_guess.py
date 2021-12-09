#!/usr/bin/env python3
# Created by: Logan Sweeney
# Created on: Dec 8, 2021
# This program asks the user to guess a number
# and if they are incorrect it will tell them, and end the game.
import random


def main():
    # Create the random number
    random_number = random.randint(1, 9)

    # Get number from user
    number_input = int(input("Guess a random number from 0-9: "))
    print("")

    # Check to see if they got the right number or wrong
    if number_input == random_number:
        print("Correct!!")
    elif number_input > 9:
        print("Too high... Why would you even try that?")
    else:
        print("Incorrect... My favorite number is {}. "
              .format(random_number))


if __name__ == "__main__":
    main()
