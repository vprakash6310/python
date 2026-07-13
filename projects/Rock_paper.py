import random

print("Welcome to the Rock Paper Scissors game!\n")
print("Rules!\nRock beats Scissors.\nScissors beats Paper.\nPaper beats Rock .\nTie: If both players throw the exact same shape, it is a tie.\n")
print("Let's play Rock Paper Scissors!\n")
print("What you choose!, type 0 for rock, 1 for paper, 2 for scissors.\n")
rock='''
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''


paper=''' 
  _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''



scissors=''' 
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

choice_me=int(input("Choose your number"))
if choice_me >=3:
    print("You entered invalid number")


print(choice_me)
if choice_me == 0:
    print("Rock",rock)
elif choice_me == 1:
    print("Paper",paper)
elif choice_me == 2:
    print("Scissors",scissors)
else:
    print("Invalid Choice")

choice_bot=random.randint(0,2)
print(f"Bot Chooses{choice_bot}")



if choice_bot == 0:
    print("Rock",rock)
elif choice_bot == 1:
    print("Paper",paper)
elif choice_bot == 2:
     print("Scissors",scissors)
else:
    print("Invalid Choice")


if choice_bot == choice_me :
    print("TIE\n Try Again")
elif choice_bot == 0 and choice_me == 1:
    print("You win!")
elif choice_bot == 0 and choice_me == 2:
    print("Bot win!")
elif choice_bot == 1 and choice_me == 2:
    print("You win!")
elif choice_bot == 1 and choice_me == 0:
    print("Bot win!")
elif choice_bot == 2 and choice_me == 0:
    print("You win!")
elif choice_bot == 2 and choice_me == 1:
    print("Bot win!")


