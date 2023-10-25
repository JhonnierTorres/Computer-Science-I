import random

# Generate a random number between 1 and 20
number_to_guess = random.randint(1, 20)

# Initialize guess count
guess_count = 0

print("Welcome to the guessing game! You have 5 attempts to guess a number between 1 and 20.")

# Your while loop goes here...
while guess_count < 5:
    guess = int(input("Enter your guess between 1 and 20: "))

    if guess == number_to_guess:
        print(f"Congratulations! you guessed the secret number ({guess})")
        break

    elif guess < number_to_guess:
        print("Try a higher number")
    else:
        print("Try lower number")

    guess_count += 1

if guess_count == 5:
    print("Sorry, you couldn't guess the secret number. The correct number was:", number_to_guess)
