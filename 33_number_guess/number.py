import random

print("Welcome to Number Guessing Game ! ")
print("I am thinking of a number between 1 to 100. Can you guess me?")
random_value = random.randint(0, 101)  # computer random number created
# print(random_value)
user_input = input("Choose a difficulty : Type 'Easy' or 'Hard'=> ").lower()
# print(user_input)

easy_choice = 10
hard_choice = 5

def chances():
    global easy_choice
    global hard_choice
    if user_input == 'easy':
        return easy_choice
    else:
        return hard_choice

finished_game = True
while finished_game == False :
    def check_number():
        user_number = int(input("Give your number : "))
        if user_number == random_value:
            print("You win")
            finished_game == True
        elif user_number > random_value:
            print("Too high")
        else:
            print("Too low")
    
    