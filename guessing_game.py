import random
def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    tries = 5

    print("I'm thinking of a number between 1 and 100.")
    guess = int(input("Guess what it is. You have " + str(tries) + " tries: "))

    while tries > 0:
        if guess == secret_number:
            print("You got it!")
            return
        else:
            tries -= 1
            if tries == 0:
                print("Nope! You lost. The number was " + str(secret_number))
                return
            elif guess < secret_number:
                guess = int(input("Nope! Too low. Try again (" + str(tries) + " tries left): "))
            else:
               guess = int(input("Nope! Too high. Try again (" + str(tries) + " tries left): "))


def main():
    play_again = "y"
    while play_again == "y":
        play_game()
        print("Do you want to play again? (Y/N): ", end="")
        play_again = input().strip().lower()
    print("Thanks for playing!", end=" \n")

if __name__ == "__main__":

    print('From guessing_game')
