from turtle import Turtle, Screen 

import random
is_race_on = False

screen = Screen()
screen.setup(width=500,height=400)
user_input = screen.textinput(title="Place your bet: ",prompt = "Which color turtle win the race : ")
print(user_input)
color = ["red","orange","yellow","green","blue","purple"]
all_turtle =[]

y_position = [-70,-40,-10,20,50,80]
for i in range(0,6):
    tom  = Turtle(shape="turtle")
    tom.color(color[i])
    tom.penup()
    tom.goto(x=-230,y=y_position[i])
    all_turtle.append(tom)

if user_input:
    is_race_on= True
while is_race_on:
    
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"you have won! your winning color is {winning_color}")
            else:
                print(f"you have lost! your winning color is {winning_color}")
        distance = random.randint(0,10)
        turtle.forward(distance)
    
screen.exitonclick()