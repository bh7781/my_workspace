from common.utility import get_valid_input
import random

# https://wrpsa.com/official-rules-and-regulations-for-professional-rock-paper-scissors/
# Rock wins against Scissors.
# Scissors wins against Paper.
# Paper wins against Rock.

# ASCII Codes: https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

rock = """
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]

user_choice = get_valid_input(prompt='What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors?: ',
                              valid_choices=[0, 1, 2],
                              cast_type=int)
print(f"\n\nUser chose: \n{choices[user_choice]}")

computer_choice = random.randint(0, len(choices) - 1)
print(f"Computer chose: \n{choices[computer_choice]}")

if user_choice == computer_choice:
    print("Game Tied! Play Again!")

elif user_choice == 0:
    if computer_choice == 2:
        print("You Win!")
    else:
        print("Computer Wins!")

elif user_choice == 1:
    if computer_choice == 0:
        print("You Win!")
    else:
        print("Computer Wins!")

elif user_choice == 2:
    if computer_choice == 1:
        print("You Win!")
    else:
        print("Computer Wins!")
