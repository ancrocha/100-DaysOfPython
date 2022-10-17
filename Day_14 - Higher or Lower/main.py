# logo
# Compare A: Taylor Swift, a Musician, from United States.
# vs logo
# Against B: Selena Gomez, a Musician and actress, from United States.
# Who has more followers? Type 'A' or 'B':

# clear

# logo
# You're right! Current score: 1.
# again

# logo
# Sorry, that's wrong. Final score: 1

from re import A
from secrets import choice
from game_data import data
from art import logo, vs
import random
import os

def getnumber():
    a = random.randint(0, len(data) -1)
    b = random.randint(0, len(data) -1)
    if a == b:
        getnumber()
    else:
        return a, b

def choice_fun():
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == "a":
        return str("A")
    elif choice == "b":
        return str("B")
    elif choice != str("A") or choice != str("B"):
        print("Please choose the right option. TYPE 'A' or 'B'")
        choice_fun()
    

game_on = True

while game_on == True:

    num_a, num_b = getnumber()

    print(logo)

    print(f"Compare A: {data[num_a]['name']}, a {data[num_a]['description']}, from {data[num_a]['country']}")
    print(vs)
    print(f"Against B: {data[num_b]['name']}, a {data[num_b]['description']}, from {data[num_b]['country']}")

    user_choice = choice_fun()

    print(user_choice)

    if user_choice == "A":
        if int(data[num_a]['follower_count']) >= int(data[num_b]['follower_count']):
            print("user win")
        else:
            print("user lost")
            game_on = False
    else:
        if int(data[num_a]['follower_count']) <= int(data[num_b]['follower_count']):
            print("user win")
        else:
            print("user lost")
            game_on = False

    print(data[num_a]['follower_count'])
    print(data[num_b]['follower_count'])
