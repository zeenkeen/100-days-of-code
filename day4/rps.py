import random


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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissor]
user_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissor.\n"))
if user_choice >= 3:
    print("Invalid entry, RETRT")
else:
    print(game_image[user_choice])
    computer_choice = random.randint(0,2)
    print(f"computer chose {game_image[computer_choice]}")
    if user_choice == 0 and computer_choice == 2:
        print("You won!")
    elif computer_choice == 1 and user_choice == 0:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose!")
    elif computer_choice == user_choice:
        print("It's a draw")
  
