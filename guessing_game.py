import random


def play_game():
    """
    Runs one session of the guessing game.
    The computer chooses a random number between 1 and 100.
    The player has 5 tries to guess the number correctly.
    After each guess, the program tells the player if the guess
    was too high or too low. If the player runs out of tries, the
    correct number is revealed.
    Authors name = Elayne Vilela
    """
    play_again = "y"


    while play_again == "y":
        secret_number = random.randint(1, 100)
        tries = 5
        guessed = False

        print("I'm thinking of a number between 1 and 100.")
        guess = int(input("Guess what it is. You have " + str(tries) + " tries: "))

        while tries > 0 and not guessed:
            if guess == secret_number:
                print("You got it!", end=" \n")
                guessed = True
            else:
                tries -= 1
                if tries == 0:
                    print("Nope! You lost. The number was " + str(secret_number), end=" \n")
                elif guess < secret_number:
                    guess = int(input("Nope! Too low. Try again (" + str(tries) + " tries left): "))
                else:
                    guess = int(input("Nope! Too high. Try again (" + str(tries) + " tries left): "))

        print("Do you want to play the guessing game again? (Y/N): ", end="")
        play_again = input().strip().lower()

    print("Thanks for playing!")  # When the loop ends (user typed "n"), print the goodbye message


def main():
    """
    Entry point for the guessing game when run directly.
    """
    play_game()


if __name__ == "__main__":
    print('From guessing_game')