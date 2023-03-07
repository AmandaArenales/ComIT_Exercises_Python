"""Develop an algorithm for a dice game. The player must bet on a number between 1 and 6 (keyboard reading), 
then you must simulate the roll of a dice and finally inform the player if he has won or lost (print on screen)."""

import random

def dice_game():
    number_bet = int(input("Please, insert a number between 1 and 6: "))

    dice_roll = random.randint(1, 6)
    print(f"The roll of a dice was: {dice_roll}.")

    if number_bet == dice_roll:
        print("You won! Congratulations!!!")
    else:
        print("Sorry, you lost!")

dice_game()
