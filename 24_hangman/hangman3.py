

import random

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
=========''', '''
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

import random
word_list = ["Ram","Krishna","Shivam"]
choosen = random.choice(word_list)
print(f"choosen word is {choosen}")

###########
lives = 6

display = []
for letter in choosen:
    display += "_"
print(display)

end_of_game = False
while end_of_game==False:
    user_input = input("Guess a letter! ").lower()
    for position in range(len(choosen)):
        letter = choosen[position]
        # print(f"Current position : {position}\n Current letter :{letter}\n Guesses letter :{user_input}")
        if letter == user_input:
            display[position] = letter
    if user_input not in choosen:
        lives -= 1
        if lives ==0:
            end_of_game = True
            print("you loose")     
    
    print(f"{' '.join(display)}")###
    
    if "_" not in display:
        end_of_game = True
        print("You win")
    print(stages[lives])