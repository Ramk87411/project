from click import clear
import logo_file
import random
from data import data

# print(logo_file.logo)
# print(logo_file.vs)

def get_random_data():
    """get the random data from data list """
    # print(random.choice(data))
    return random.choice(data)

def arranged_data(account):
    """will print data in a arranged manner """
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return (f"{name}, a {description}, from {country}")

def check_followers(user_guess,a_followers,b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
def game():
    print(logo_file.logo)
    
    continue_game = True
    score = 0
    account_a = get_random_data()
    account_b = get_random_data()
    
    
    while continue_game:
        account_a = account_b
        account_b = get_random_data()
        
        while account_a == account_b:
            account_b = get_random_data()
            
            print(f"Compare A : {arranged_data(account_a)}.")
            print(logo_file.vs)
            print(f"Against B : {arranged_data(account_b)}.")
            
            
            user_guess = input("Who has more followers 'A' or 'B' : ").lower()
            a_followers_count = account_a["follower_count"]
            # print(a_followers_count)
            b_followers_count = account_b["follower_count"]
            # print(b_followers_count)
            check_followers(user_guess,a_followers_count,b_followers_count)
            
            clear()
            print(logo_file.logo)
            if check_followers:
                score += 1
                print(f"You are right , your score is{score}")
            else:
                print(f"Your are wrong , your final score is {score} ")
            
game()
