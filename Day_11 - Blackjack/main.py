import random
from art import logo
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(list_of_cards):
    if len(list_of_cards) == 2 and sum(list_of_cards) == 21:
        return 0
    elif 11 in list_of_cards and sum(list_of_cards) < 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
        return sum(list_of_cards)
    else:
        return sum(list_of_cards)


def compare(user, computer):
    if user == computer:
        return "draw"
    elif computer == 0:
        return "computer"
    elif user == 0:
        return "user"
    elif user > 21:
        return "computer"
    elif computer > 21:
        return "user"
    elif user > computer:
        return "user"
    else:
        return "computer"


def blackjack():

    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)

        player_cards = []
        computer_cards = []
        player_cards.append(deal_card())
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
        computer_cards.append(deal_card())

        game_is_on = True

        while game_is_on:
            player_score = calculate_score(player_cards)
            computer_score = calculate_score(computer_cards)

            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            if computer_score == 21 or player_score > 21:
                game_is_on = False
            else:
                another_card = input(
                    "Type 'y' to get another card, type 'n' to pass:? ")
                if another_card == "y":
                    player_cards.append(deal_card())
                    player_score = calculate_score(player_cards)
                else:
                    game_is_on = False

        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        print(
            f"Your's final hand: {player_cards}, final score: {player_score}")

        print(
            f"Computer's final hand: {computer_cards}, final score: {computer_score}")

        winer_is = compare(player_score, computer_score)

        print(f"The winner is: {winer_is}")

        blackjack()

    else:
        exit()


blackjack()
