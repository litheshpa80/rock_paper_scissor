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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]
use=int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if use>=0 and use<=2:
    print("You chose:")
    print(game[use])
computer=random.randint(0,2)
print("Computer chose:")
print(game[computer])
if use>=3 or use<0:
    print("Invalid number")
elif use== 0 and computer==2:
    print("you win")
elif computer>use:
    print("You lose")
elif computer==use:
    print("It's a draw")
elif computer<use:
    print("You win")


