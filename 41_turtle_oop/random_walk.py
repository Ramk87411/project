from turtle import Turtle, Screen
import turtle
import random


color = ["silver", "chartreuse", "goldenrod", "pink", "purple", "red"]
# walk = True
# tom = Turtle()
# tom.width(5)
# tom.speed(5)

# while walk:
#     tom.forward(random.randint(0, 100))
#     tom.color(random.choice(color))
#     tom.right(90)

turtle.colormode(255)  # for rgb mode


def random_color():  # for unlimited color mode from the color pallet
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tom = Turtle()
direction = [0, 90, 180, 270]
tom.width(10)
tom.speed("fastest")
for i in range(200):
    tom.color(random_color())
    tom.forward(30)
    tom.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()
