import random

def get_value(text):
    '''Returns the input as an integer if the string can be turned into an integer, and a string otherwise.'''
    try:
        return int(text)
    except:
        return text

def get_decision(message, *args):
    '''Returns the decision of the user. Checks if the user enters an invalid input based on parameters
    provided and prompts the user to try again until they enter a valid input.'''
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

def game():
    '''Play rock, paper, scissors with the user until they say they want to stop.'''
    # set initial decision to 'y' because they just chose this game in the main class
    decision = 'y'

    # keep running the loop while the user keeps saying 'yes'
    while (decision == 'y'):
        # user makes their selection
        print('Enter your choice: 1 paper, 2 scissors, 3 rock: ', end='')
        num_user = get_decision('Enter your choice: 1 paper, 2 scissors, 3 rock', 1, 2, 3)

        # computer makes its selection
        num_computer = random.randint(1, 3)

        # calculate winner (1 beats 3, 2 beats 1, 3 beats 2)
        if (num_user == 1):
            if (num_computer == 1):
                print('It is a tie!')
            elif (num_computer == 2):
                print('You lose!')
            elif (num_computer == 3):
                print('You win!')

        elif (num_user == 2):
            if (num_computer == 1):
                print('You win!')
            elif (num_computer == 2):
                print('It is a tie!')
            elif (num_computer == 3):
                print('You lose!')

        elif (num_user == 3):
            if (num_computer == 1):
                print('You lose!')
            elif (num_computer == 2):
                print('You win!')
            elif (num_computer == 3):
                print('It is a tie!')

        # ask the user if they want to play Rock-Paper-Scissors again
        print('Do you want to play Rock-Paper-Scissors again? (y/n): ', sep='', end='')
        decision = get_decision('Do you want to Rock-Paper-Scissors again? (y/n)', 'y', 'n')
        print()

if __name__ == "__main__":
    game()