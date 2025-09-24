import random
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
    while play_again == "y":      #loops the game to run again if the user keeps saying y to play the game
        secret_number = random.randint(1, 100)
        tries = 5
        guessed = False

        print("I'm thinking of a number between 1 and 100.")
    
        guess = None
        valid = False
        while not valid:  #loop until it gets a valid number in case the user inputs an invalid value
            user_input = input(f"Guess what it is. You have {tries} tries: ")
            
            if user_input.isdigit():  # checks if all characters are numbers
                guess = int(user_input)
                valid = True
            else:
                print("Please enter a valid number between 1 and 100.")
                
        
        while tries > 0 and not guessed:         #The loop keeps running as long as the player still has tries left AND hasn’t guessed the number yet. 
            if guess == secret_number:           
                print("You got it!")    #If guessed ever becomes True, the loop ends immediately.
                guessed = True
            else:
                tries -= 1
                if tries == 0:
                    print("Nope! You lost. The number was " + str(secret_number))
                else:
                    #chechs input validation again
                    valid = False
                    while not valid:
                        user_input = input(
                            ("Nope! Too low. " if guess < secret_number else "Nope! Too high. ")
                            + "Try again (" + str(tries) + " tries left): ")
                        if user_input.isdigit():
                            guess = int(user_input)
                            valid = True
                        else:
                            print("Please enter a valid number between 1 and 100.")

        play_again = input("Do you want to play the guessing game again? (Y/N): ").strip().lower()
    
    print("Thanks for playing!")  

def main():
    """
    Entry point for the guessing game when run directly.
    Author = Elayne
    """
    play_game()

if __name__ == "__main__":
    play_game()


