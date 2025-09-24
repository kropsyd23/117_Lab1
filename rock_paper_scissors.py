import random
import main

def play_game():
    '''Play rock, paper, scissors with the user until they say they want to stop.
    Author: Sydney'''
    # set initial decision to 'y' because they just chose this game in the main class
    decision = 'y'

    # keep running the loop while the user keeps saying 'yes'
    while (decision == 'y'):
        # user makes their selection
        print('Enter your choice: 1 rock, 2 paper, 3 scissors: ', end='')
        num_user = main.get_decision('Enter your choice: 1 rock, 2 paper, 3 scissors', 1, 2, 3)

        # computer makes its selection
        num_computer = random.randint(1, 3)

        # calculate winner (1 beats 3, 2 beats 1, 3 beats 2)
        if (num_user == 1):
            if (num_computer == 1):
                print('I chose rock. It is a tie!')
            elif (num_computer == 2):
                print('Paper beats rock. You lose!')
            elif (num_computer == 3):
                print('Rock beats scissors. You win!')

        elif (num_user == 2):
            if (num_computer == 1):
                print('Paper beats rock. You win!')
            elif (num_computer == 2):
                print('I chose paper. It is a tie!')
            elif (num_computer == 3):
                print('Scissors beats paper. You lose!')

        elif (num_user == 3):
            if (num_computer == 1):
                print('Rock beats scissors. You lose!')
            elif (num_computer == 2):
                print('Scissors beats paper. You win!')
            elif (num_computer == 3):
                print('I chose scissors. It is a tie!')

        # ask the user if they want to play Rock-Paper-Scissors again
        print('Do you want to play Rock-Paper-Scissors again? (y/n): ', sep='', end='')
        decision = main.get_decision('Do you want to Rock-Paper-Scissors again? (y/n)', 'y', 'n')
        print()

if __name__ == "__main__":
    play_game()