"""
Lab 1
Group 7
Authors: Sydney Kropf, Elayne Vilela
Date: 09/18/2025
"""

import rock_paper_scissors
import guessing_game

def get_value(text):
    """
    Returns the input as an integer if the string can be turned into an integer, and a string otherwise.
    Author: Sydney
    """

    try:
        return int(text)
    except:
        return text

def get_decision_range(message, min, max):
    """
    Returns the decision of the user when the valid input is a range of integers.
    Checks if the user inputted an integer in the range [min, max].
    If input was not valid, continue prompting the user to try again until it is valid.
    Author: Sydney
    """

    num = input()

    # continue prompting the user to try again until they enter a valid input
    matches = False
    while (matches == False):
        try:
            # num will be converted into an integer if an integer was inputted, otherwise remain a string
            num = get_value(num)
            # check if the input is in [min, max]
            # will cause an error if the input was not an integer to enter the catch
            if (num >= min and num <= max):
                matches = True # change matches to True to exit the while loop

            # if it is not between 1 and 100, raise an error to enter the catch
            else:
                raise ValueError()

        # if the input was not an integer or an integer outside of [min, max], prompt the user to try again
        except:
            print('Please enter a valid input! ', message, ': ', sep='', end='')
            num = input()

    return num

def get_decision(message, *args):
    """
    Checks if the user enters an input that matches the parameters provided.
    Prompts the user to try again until they enter a valid input.
    Returns the decision of the user once it is a valid input.
    Author: Sydney
    """

    text = get_value(input())
    matches = False

    # remain in this loop until the input matches one of the valid inputs
    while (matches == False):
        # check if the input matches any of the valid inputs
        for n in args:
            if (text == n):
                matches = True

        # if the input is invalid, send an error message and take a new value
        if (matches == False):
            print('Please enter a valid input! ', message, ': ', sep='', end='')
            text = get_value(input())

    return text

def main():
    """
    Let the user choose which game they want to play.
    Repeat until they don't want to play anymore.
    Author: Sydney and Elayne
    """

    # welcome message
    print('Welcome! You will get the chance to play two different games as many times as you want!')
    print('Guessing Game is a game where you try to guess a number between 1 and 100.')
    print('Rock-Paper-Scissors is a game where rock beats scissors, scissors beats paper, and paper beats rock.')
    print()


    # while the user wants to keep playing, continue prompting them to play more games
    num = 0
    while (num != 3):
        print('Which game do you want to play? 1 Guessing Game, 2 Rock-Paper-Scissors, 3 None: ', end='')
        num = get_decision_range('Which game do you want to play? 1 Guessing Game, 2 Rock-Paper-Scissors, 3 None', 1, 3)
        print()

        # play Guessing Game
        if (num == 1):
            guessing_game.play_game()
            print()

        # play Rock-Paper-Scissors
        elif (num == 2):
            rock_paper_scissors.play_game()

    print('Have a great day!')

if __name__ == "__main__":
    main()