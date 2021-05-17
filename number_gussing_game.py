#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Sat/May15/2021
# This program is number guessing game using while loop


import random


def main():
    # this function checks if the number guessed is correct or wrong

    # input
    guessed_number_as_string = input("Enter the number between 1 - 9:")
    random_number = random.randint(1, 9)  # a number between 1 and 9

    # process & output
    try:
        guessed_number = int(guessed_number_as_string)

        while True:
            if (guessed_number == random_number):
                print("\nYou guessed correct!")
                print("Thanks for playing.")
                print("\nDone.")
                break
            else:
                print("You guessed Wrong!")
                guessed_number = int(input("Enter the number again 1 - 9:"))

    except Exception:
        print("\ninvalid input!")
        print("\nDone.")


if __name__ == "__main__":
    main()
