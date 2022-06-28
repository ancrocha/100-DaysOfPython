import random
import sys
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(
    input("What do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

computer_choice = random.randint(0, 2)

print(computer_choice)


if user_choice == computer_choice:

if user_choice == 0:
    print(rock)
    print("\n")
    if computer_choice == 0:
        print("Computer chose: \n")
        print(rock)
        print("")
        print("Tie!")
    elif computer_choice == 1:
        print("Computer chose: \n")
        print(paper)
        print("")
        print("You lose")
    else:
        print("Computer chose: \n")
        print(scissors)
        print("")
        print("You Win")
elif user_choice == 1:
    print(paper)
    if computer_choice == 0:
        print("Computer chose: \n")
        print(rock)
        print("")
        print("You Win!")
    elif computer_choice == 1:
        print("Computer chose: \n")
        print(paper)
        print("")
        print("Tie!")
    else:
        print("Computer chose: \n")
        print(scissors)
        print("")
        print("You lose")
elif user_choice == 2:
    print(scissors)
    if computer_choice == 0:
        print("Computer chose: \n")
        print(rock)
        print("")
        print("You Lose")
    elif computer_choice == 1:
        print("Computer chose: \n")
        print(paper)
        print("")
        print("You Win")
    else:
        print("Computer chose: \n")
        print(scissors)
        print("")
        print("Tie!")
else:
    print("wrong coice.")
    sys.exit("aa! errors!")
