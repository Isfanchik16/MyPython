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
    _____
---'   __)______
          ______)
          _______)
         _______)
---.__________)
'''
scissor = '''
    _____
---'   __)______
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock,paper,scissor]
my_choice = int(input('''Welcome to the game : Rock , Paper , Scissor And now.
Your choice, Please choose: Rock (0), Paper (1), Scissors (2) >>'''))
print(f"Your choice is {options[my_choice]}")
comp_choice = random.choice(options)
print(f"Computer choice is {comp_choice}")
if options[my_choice] in options:
    if options[my_choice] == comp_choice:
            print("""                                    
         DDDD   RRRR     A     W     W  |
         D   D  R   R   A A    W     W  |
         D   D  RRRR   A   A   W  W  W  |
         D   D  R R    AAAAA   W W W W  |
         DDDD   R  RR  A   A   W     W  .
                                         
    """)
    elif (my_choice==0 and comp_choice==scissor) or (my_choice==1 and comp_choice==rock) or (my_choice==2 and comp_choice==paper):
        print(""" The outcome is
         Y   Y   OOO   U   U     W   W   OOO   N   N  |
          Y Y   O   O  U   U     W   W  O   O  NN  N  |
           Y    O   O  U   U     W W W  O   O  N N N  |
           Y    O   O  U   U     WW WW  O   O  N  NN  |
           Y     OOO    UUU      W   W   OOO   N   N  .
    """)
    else:
         print(""" The outcome is
         Y   Y   OOO   U   U       L       OOO   SSS   EEEEE |
          Y Y   O   O  U   U       L      O   O  S      E    |
           Y    O   O  U   U       L      O   O   SSS   EEEE |
           Y    O   O  U   U       L      O   O      S  E    |
           Y     OOO    UUU        LLLLL   OOO   SSS   EEEEE .
""")

