# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
days = (90-age)*365
# print(days)
weeks = (90-age)*52
# print(weeks)
month = (90-age)*12
# print(month)
#adding f in below print statement convert it into f-string (search for f-string in python)
print(f"You have {days} days, {weeks} weeks,and {month} months left")