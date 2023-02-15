# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

print("Welcome to pizza delivery !")
size = input("What size of pizza do you want? S, M, L: ")
add_pepperoni = input("Do you want to add pepperoni? Y or N: ")
extra_cheese = input("Do you want to add extra cheese? Y or N: ")
bill = 0

# if size == "S":
#     bill += 15
#     print(f" your Small pizza cost:{bill} ")
#     if add_pepperoni == "Y":
#         bill += 3
#         if extra_cheese == "Y":
#             bill += 1
#             print(f"you Small pizza+ add_pepperoni+extra_cheese cost :{bill}")
#     else:
#         if extra_cheese == "Y":
#             bill += 1
#             print(f"Your Small_pizza and chesse cost :{bill} ")


if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"your final bill is ${bill}")
