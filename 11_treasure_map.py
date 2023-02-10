# Treasure map exercise
"""
You are going to write a program that will mark a spot with an X.
In the starting code, you will find a variable called map.
This map contains a nested list. When map is printed this is what the nested list looks like:
[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}" to format the 3 lists to be printed as a 3 by 3 square, each on a new line. 
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
Now it looks a bit more like the coordinates of a real map:

Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
The first digit in the input will specify the column (the position on the horizontal axis).
The second digit in the input will specify the row number (the position on the vertical axis). 
So an input of 23 should place an X at the position shown below:

First, your program must take the user input and convert it to a usable format.
Next, you need to use that input to update your nested list with an "x". Remember that your nested list map actually looks like this: [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']].
"""
####################################################################
# print("Welcome to Treasure Map exercise !")
# row1 = ["⬜️", "️⬜️", "️⬜️"]
# row2 = ["⬜️", "⬜️", "️⬜️"]
# row3 = ["⬜️️", "⬜️️", "⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# first_number = int(position)//10
# second_number = int(position) % 10

# print(first_number)
# print(second_number)

# if first_number >3 :
#     exit
# else:
#     print(first_number)
# if second_number >3:
#     exit
# else:
#     print(second_number)
# # if there is input in format of (23) it will be 2,3 || 2 is row and 3 is column .so 3 will be nested list row (2) and 2 will be its (2-1) index valew marked with x .

# if second_number == 3:
#     if first_number == 1:
#         print(row3[0],"X")
#     elif first_number == 2:
#         print(row3[0],"X")
#     else:
#         print(row3[0],"X")
# elif second_number == 2:
#     if first_number == 1:
#         print(row2[0],"X")
#     elif first_number == 2:
#         print(row2[0],"X")
#     else:
#         print(row2[0],"X")
# else:
#     if first_number == 1:
#         print(row2[0],"X")
#     elif first_number == 2:
#         print(row2[0],"X")
#     else:
#         print(row2[0],"X")

##################################################################################
print("Welcome to Treasure Map exercise !")
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

row = int(position[0])
column = int(position[1])

selected_line = map[column - 1]
selected_line[row-1] = "X"
print(f"{row1}\n{row2}\n{row3}")