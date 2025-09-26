import random
import helpers  # using the helpers functions for consistency from the helpers file
def play_game():
    """
    Runs one session of the guessing game.
    The computer chooses a random number between 1 and 100.
    The player has 5 tries to guess the number correctly.
    After each guess, the program tells the player if the guess
    was too high or too low. If the player runs out of tries, the
    correct number is revealed.
    Author = Elayne Vilela
    """
    play_again = "y"
    while play_again == "y":      #loops the game to run again if the user keeps saying 'yes' to play the game
        secret_number = random.randint(1, 100) 
        tries = 5
        guessed = False         

        print("I'm thinking of a number between 1 and 100.")
        print(f"Guess what it is. You have {tries} tries: ", end="")
        guess = helpers.get_decision_range(f"Guess what it is. You have {tries} tries", 1, 100) #importing from the helpers file
            
        
        while tries > 0 and not guessed:         #The loop keeps running as long as the player still has tries left AND hasn’t guessed the number yet. 
            if guess == secret_number:           
                print("You got it!")    #If guessed ever becomes True, the loop ends immediately.
                guessed = True
            else:
                tries -= 1             #starts to countdown the amount of tries
                if tries == 0:
                    print("Nope! You lost. The number was " + str(secret_number))
                elif guess < secret_number:
                    print(f"Nope! Too low. Try again ({tries} tries left): ", end="")
                    guess = helpers.get_decision_range(f"Nope! Too low. Try again ({tries} tries left)", 1, 100) #imports get_decision from helpers to check the user valid input
                else:
                    print(f"Nope! Too high. Try again ({tries} tries left): ", end="")
                    guess = helpers.get_decision_range(f"Nope! Too high. Try again ({tries} tries left)", 1, 100) #imports get_decision from helpers to check the user valid input

        print("Do you want to play the guessing game again? (y/n): ", end="")
        play_again = helpers.get_decision("Do you want to play the guessing game again? (y/n)", 'y', 'n')

    print("Thanks for playing!")  #When the loop ends (user typed "n"), print the goodbye message


def main():
    """
    Entry point for the guessing game when run directly.
    Authors: Elayne
    """
    play_game()


if __name__ == "__main__":
    main()
