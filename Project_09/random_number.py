import random

computer_guess = random.randint(1,100)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
is_running=True
print(computer_guess)
while is_running:
    your_guess = int(input("The computer thought of a number, find that number (1,100) : "))
    if your_guess == computer_guess and lives>0:
        print(""" 
         Y   Y   OOO   U   U     W   W   OOO   N   N  |
          Y Y   O   O  U   U     W   W  O   O  NN  N  |
           Y    O   O  U   U     W W W  O   O  N N N  |
           Y    O   O  U   U     WW WW  O   O  N  NN  |
           Y     OOO    UUU      W   W   OOO   N   N  .
    """)
        quit = input("Do you want play again? (Yes or No) : ").lower()
        if quit == "yes":lives=7
        else:
          is_running = False
          print("Your previous game was not bad?")
    elif computer_guess > your_guess and lives>0:
        lives -=1
        print("That was a bigger number!",stages[lives])
        
    elif computer_guess < your_guess and lives>0:
        lives -=1
        print("That was a smaller number!",stages[lives])
    else:
        print(f"The computer thought '{computer_guess}'")
        print(""" 
         Y   Y   OOO   U   U     L      OOO   SSS   EEEEE |
          Y Y   O   O  U   U     L     O   O  S     E     |
           Y    O   O  U   U     L     O   O   SSS  EEEE  |
           Y    O   O  U   U     L     O   O     S  E     |
           Y     OOO    UUU      LLLLL  OOO   SSS   EEEEE .
    """)
        quit = input("Do you want play again? (Yes or No) : ").lower()
        if quit == "yes":lives=7
        else:
            is_running = False
