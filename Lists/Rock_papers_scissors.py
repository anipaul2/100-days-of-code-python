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

import random
user = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissor. \n"))
computer = random.randint(0, 2)

choices = [rock, paper, scissors]
print(choices[user])
print("The computer threw: \n")
print(choices[computer])

if ((user + 1) % 3 == 0):
    print("you lost!")
elif (user == computer):
    print("It's a draw!")
else:
    print("You lose!")