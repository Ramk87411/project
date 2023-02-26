import random

easy_choice = 10
hard_choice = 5

def check_guess_number(random_number,user_guess,turns):
    if random_number > user_guess:
        print("Too low")
        return turns - 1
    elif random_number < user_guess:
        print("Too high")
        return turns - 1
    else:
        print(f"your answer is {random_number}")

def difficuilty():
    level = input("Choose a difficuilty level : type 'easy' or 'hard' :").lower()
    if level == 'easy':
        return easy_choice
    else:
        return hard_choice

def game():
    print("Welcome to number guessing game ")
    print("I have guessd a number between 1 to 100 : ")
    random_number = random.randint(1,100)
    print(f"your answer is {random_number}")
    turns = difficuilty()
    
    user_guess = 0
    while user_guess != random_number:
        print(f"you have {turns} attempt remaining to guess a number . ")
        user_guess = int(input("make a guess:"))
        turns = check_guess_number(random_number,user_guess,turns)
        if turns == 0:
            print("You have run out of turns , you loose ")
            return
        else:
            print("guess again")

game()