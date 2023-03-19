from turtle import Turtle, Screen
import time




screen =  Screen()
screen.setup(600,600) # game board size
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)


# sn1 = Turtle()
# sn1.shape("square")
# sn1.color("white")
# sn1.goto(0,0)
# sn2 = Turtle()
# sn2.shape("square")
# sn2.color("white")
# sn2.goto(-20,0)
# sn3 = Turtle()
# sn3.shape("square")
# sn3.color("white")
# sn3.goto(-40,0)

start_position = [(0,0),(-20,0),(-40,0)]
segments = []


for position in start_position:
    sn1=Turtle()
    sn1.shape("square")
    sn1.color("white")
    sn1.penup()
    sn1.goto(position)
    segments.append(sn1)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)
    for seg_num in range(len(segments)-1,0,-1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)


screen.exitonclick()