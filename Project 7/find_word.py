import random

words_list=["hello","hi","welcome","good","feeling"]

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

unknown_word = []
random_choice = random.choice(words_list)
for x in random_choice:
    unknown_word.append("-")
print(unknown_word)

lives = 6
while lives !=0:
    guess_letter = input("Guess a letter >>").lower()

    if guess_letter in unknown_word:
        print(f"You have already guessed this '{guess_letter}' letter!")

    for x in range(len(random_choice)):
        if random_choice[x] == guess_letter:
            unknown_word[x] = guess_letter
    print(unknown_word)

    if guess_letter not in random_choice:
        lives -=1
        print(stages[lives])
    else:
        print(stages[lives])


if lives >0:
    print(""" 
         Y   Y   OOO   U   U     W   W   OOO   N   N  |
          Y Y   O   O  U   U     W   W  O   O  NN  N  |
           Y    O   O  U   U     W W W  O   O  N N N  |
           Y    O   O  U   U     WW WW  O   O  N  NN  |
           Y     OOO    UUU      W   W   OOO   N   N  .
    """)

else:
    print(""" 
         Y   Y   OOO   U   U       L       OOO   SSS   EEEEE |
          Y Y   O   O  U   U       L      O   O  S      E    |
           Y    O   O  U   U       L      O   O   SSS   EEEE |
           Y    O   O  U   U       L      O   O      S  E    |
           Y     OOO    UUU        LLLLL   OOO   SSS   EEEEE .
    """)
    print(f"The word was '{random_choice}'")
    
