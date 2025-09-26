"""
Lab 1
Group 7
Authors: Sydney Kropf, Elayne Vilela
Date: 09/18/2025
"""

import rock_paper_scissors
import guessing_game

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
        from helpers import get_decision_range
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
