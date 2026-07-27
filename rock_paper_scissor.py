'''
WORKFLOW OF PROEJCT

import random module
user input (USER WILL ENTER HIS/HER CHOICE)
computer choice (COMPPUTER WILL CHOOSE RANDOMLY)
result print

Cases 

1 - rock
rock - rock = tie
rock - paper = paper wins
rock - scissor = rock wins

2- paper
paper - paper = tie
paper - scissor = scissor wins
paper - rock =  paper wins

3 - scissor
scissor - scissor = tie
scissor - rock = rock wins
scissor - paper = scissor wins

'''

import random

def game():
    item_list = ["rock", "paper", "scissor"]

    user_choice = input("Enter your choice (Rock, Paper, Scissor): ").lower()

    if user_choice not in item_list:
        print("Invalid choice! Try again.")
        return

    comp_choice = random.choice(item_list)

    print(f"Computer choice = {comp_choice}")
    print(f"User choice = {user_choice}")

    if user_choice == comp_choice:
        print("It's a tie!")

    elif user_choice == "rock":
        if comp_choice == "paper":
            print("Computer wins!")
        else:
            print("You win!")

    elif user_choice == "paper":
        if comp_choice == "scissor":
            print("Computer wins!")
        else:
            print("You win!")

    elif user_choice == "scissor":
        if comp_choice == "rock":
            print("Computer wins!")
        else:
            print("You win!")

game()