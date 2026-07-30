import random

# Generate a secret number between 1 and 100
secret_number = random.randint(1,100)
guess = None

print("I'm thinking of a number between 1 and 100. Can you guess it?")

# Keep looping until the user guesses correctly
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed the secret number.")
