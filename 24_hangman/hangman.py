import random

print("Welcome to the hangman Game!")
word_list = ["Ram","Krishna","Shivam"]
choosen = random.choice(word_list)
user_input = input("Guess a letter! ").lower()
for letter in choosen:
    if letter == user_input:
        print("Right")
    else:
        print("Wrong")
