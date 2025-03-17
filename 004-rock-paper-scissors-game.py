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
choices_list = [rock, paper, scissors]
my_choice = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(f"Your Choice\n{choices_list[my_choice]}")
machine_choice = random.randint(0, 2)
print(f"Computer choose\n{choices_list[machine_choice]}")

if my_choice == 0 and machine_choice == 2:
    print("You Win")
elif my_choice == 1 and machine_choice == 0:
    print("You won")
elif my_choice == 2 and machine_choice == 1:
    print("You Win")
elif my_choice == machine_choice:
    print("Draw")
else:
    print("You Lose")
