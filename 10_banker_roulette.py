# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.

"""
Algorithm:
1- split the string that entered by users
2-length of the list
3-random integer pickup
4-list[random_integer]
5-print the list[random_integer ]
"""
import random
print(" Welcome to Banker Roulette game. ")
name = input("Enter your particiants name !  Use(,)for seprating name \n")
up_name = name.split(",")

length = len(up_name)
# random_number = random.randint(0,length)
random_number = random.randint(0,length-1) # beacus it start with 0 so reduce 1 from total length .
choice_name = up_name[random_number]
print(f"{choice_name} have to pay todays bill !")

# or using choice()
choice_name2 = random.choice(up_name) 
print(f"{choice_name2} have to pay todays bill !")