"""
# print max value in a list (not to use max function , use for loop)
You are going to write a program that calculates the highest score from a List of scores.
e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
Important you are not allowed to use the max or min functions. The output words must match the example. i.e
The highest score in the class is: x
"""
print(" Welcome to Max value coding challenge")
values = input("Enter your value !").split() # split will seprate each value from the string 
for i in range(0,len(values)):
    values[i] = int(values[i])
print(values) # this for loop convert the string in to int value 

highest_value = 0
for i in values:
    if i > highest_value:
        highest_value = i
print(f"Your highest score is {highest_value}")