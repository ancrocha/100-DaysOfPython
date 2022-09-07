import os
from time import sleep
from art import logo


def clear():
    return os.system('cls')


bids = {}

play_again = True

print(logo)

while play_again:
    name = input("What is your name: ")
    bid = input("What is your bid price: $")
    bids[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if other_bidders == "no":
        play_again = False
        max_key = max(bids, key=bids.get)
        max_value = max(bids.values())
    else:
        clear()

print(f"The winner is {max_key} with a bid of ${max_value}")
