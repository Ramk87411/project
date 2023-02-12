"""
# avg height calculator
You are going to write a program that calculates the average student height from a List of heights.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
The average height can be calculated by adding all the heights together and dividing by the total number of heights.
e.g.
180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
There are a total of 7 heights in student_heights
1146 ÷ 7 = 163.71428571428572
Average height rounded to the nearest whole number = 164
Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.
"""

print(" Welcome to Average height calculator !")
height = input("Enter your height followed by tab_space !")
up_height = height.split()
print(up_height)

for n in range(0,len(up_height)):
    up_height[n] = int(up_height[n])
    # print(up_height)
# sum function work
#  sum = 0
# for i in range (0,len(up_height)):
#     sum = sum+up_height[i]
# print(sum)
total_height = 0
for i in up_height:
    total_height = total_height+i
print(total_height)
#len function work
no=0
for i in (up_height):
    no = no+1
print(no)
avg_height = round(total_height/no)
print(avg_height)
# avg_height = sum(up_height)//len(up_height)
# print(avg_height)
