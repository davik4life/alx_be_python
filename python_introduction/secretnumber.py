import random

guesses = 0
secret_number = random.randint(1, 10)

game_ongoing = True

while game_ongoing:
    guess = int(input("Guess a number between 1 and 10: "))

    match guess:
        case n if n == secret_number:
            print("Congratulations, you guessed it!")
            guesses += 1
            print(guesses, "guess(es) taken.")
            game_ongoing = False
            print("Game Over. Thanks for playing!")
            print("Developed by Victor Adeshile.")
            repeat = input("Would you like to play again? (yes/no): ").strip().lower()
            if repeat == "yes":
                secret_number = random.randint(1, 10)
                guesses = 0
                game_ongoing = True
            else:
                print("Goodbye!")

        case n if n > secret_number:
            print("Oops, your guess is a bit high. Try again!")
            guesses += 1

        case n if n < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")
            guesses += 1

        case _:
            print("That's not a valid number. Please enter a number between 1 and 10")


    