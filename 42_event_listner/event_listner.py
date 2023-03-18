from turtle import Turtle, Screen
tom = Turtle()
screen = Screen()


def move_forward():
    tom.forward(20)


def back_ward():
    tom.backward(20)


def counter_clockwise():
    new_heading = tom.heading()+10
    tom.setheading(new_heading)


def clockwise():
    new_heading = tom.heading()-10
    tom.setheading(new_heading)


def circle():
    tom.circle(50)


def clear_draw():
    screen.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=back_ward)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='r', fun=circle)
screen.onkey(key='c', fun=clear_draw)
screen.exitonclick()
