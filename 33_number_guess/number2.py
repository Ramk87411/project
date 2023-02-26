import random
#from random import randint

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def check_answer(guess, answer,turns):
    if guess > answer:
        print("Too high")
        return turns -1
    elif guess<answer:
        print("Too low")
        return turns-1
    else:
        print(f"your answer is {answer}.")

def set_difficulty():
    level = input("Choose a difficuilty . type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN


def game():
    print("Welcome to guessing game !")
    print("I am thinking of anumber between i and 100.")
    answer =  random.randint(1,100)
    # print(f"pssst, the correct answer is {answer}")
    turns = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess anumber .")
        guess = int(input("Make a guess:"))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You have run out of number , you loose.")
            return 
        else:
            print("Guess again")
game()