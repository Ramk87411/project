import turtle
import random

circle = turtle.Turtle()
circle.speed("fastest")
# circle.circle(50) # draw the circle

# random color
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

for i in range(100):
    circle.color(random_color())
    circle.circle(100)
    circle.left(10)

## from solution
# def draw_spirograph(size_of_gap):
#     for i in range(int(360/size_of_gap)):
#         circle.color(random_color())
#         circle.circle(100)
#         circle.setheading(circle.heading()+10)

# draw_spirograph(3)

screen = turtle.Screen()
screen.exitonclick()