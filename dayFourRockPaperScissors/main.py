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
print(paper)

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
human_choice = input("Rock, Paper or Scissors?")

choices = [rock, paper, scissors]
computerChoice = random.choices(choices)

if computerChoice == rock or paper or scissors:
    if human_choice == "paper":
        print("YOOO")


print(f"{computerChoice}")








# print(("""\

#                                        ._ o o
#                                        \_`-)|_
#                                     ,""       \ 
#                                   ,"  ## |   ಠ ಠ. 
#                                 ," ##   ,-\__    `.
#                               ,"       /     `--._;)
#                             ,"     ## /
#                           ,"   ##    /


#                     """))

