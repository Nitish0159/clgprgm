import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Puzzle!")
    print("I have picked a number between 1 and 100. Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You found the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid whole number.")

if __name__ == "__main__":
    number_guessing_game()
