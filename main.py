"""
Lab 1
Group 7
Authors: Sydney Kropf, Elayne Vilela
Date: 09/18/2025
"""

import rock_paper_scissors
import guessing_game

def get_decision_range(message, min, max):
    '''Returns the decision of the user when the valid input is a range of integers.
    Checks if the user inputted an integer in the range [min, max].
    If input was not valid, continue prompting the user to try again until it is valid.
    Author: Sydney'''

    # continue prompting the user to try again until they enter a valid input
    num = input()
    matches = False
    while (matches == False):
        # if the input can be turned to an integer without error, check if it is in the correct range
        try:
            num = int(num)
            if (num >= min and num <= max):
                matches = True # change matches to True to exit the while loop
            # if it is not between 1 and 100, raise an error to enter the catch
            else:
                raise ValueError()

        # if the input was not an integer or an integer outside of [1, 100], prompt the user to try again
        except:
            print('Please enter a valid input! ', message, ': ', sep='', end='')
            num = input()

    return num

def get_value(text):
    '''Returns the input as an integer if the string can be turned into an integer, and a string otherwise.
    Author: Sydney'''
    try:
        return int(text)
    except:
        return text

def get_decision(message, *args):
    '''Returns the decision of the user. Checks if the user enters an invalid input based on parameters
    provided and prompts the user to try again until they enter a valid input.
    Author: Sydney'''
    text = get_value(input())
    matches = False

    # check if the input initially passed matches one of the possible options
    for n in args:
        if (text == n):
            matches = True

    # if it doesn't match, continue prompting for a new input until it matches
    while (matches == False):
        print('Please enter a valid input! ', message, ': ', sep='', end='')
        text = get_value(input())
        for n in args:
            if (text == n):
                matches = True

    return text

def main():
    '''Let the user choose which game they want to play. Repeat until they don't want to play anymore.
    Author: Sydney and Elayne'''

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