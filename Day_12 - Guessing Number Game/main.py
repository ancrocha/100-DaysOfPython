import random


def chooseNumber():
    print("I'm thinking of a number between 1 and 100.")
    return random.randint(1, 100)


# Starts Here.
print("Welcome to the Number Guessing Game!")

number = chooseNumber()

difficulty_set = False

while not difficulty_set:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        attempts = 5
        difficulty_set = True
    elif difficulty == "easy":
        attempts = 10
        difficulty_set = True
    else:
        print("invalid choice, please try again!")

while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}")
        break
    elif guess < number:
        print("Too Low")
    else:
        print("Too high")

    attempts -= 1
    print("Guess again.")
