from turtle import Turtle,Screen 
# from turtle import * #-everything can be imported all at once by using * 

tim= Turtle()
# tim.shape("turtle")
# tim.shapesize(5)
# tim.color("red")

# # # make a square 
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# """or"""
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)
    

## draw a dash line (gap and line and gap and line )

# tom = Turtle()

# for shape in range(15):
#     tom.forward(10)
#     tom.penup()
#     tom.forward(10)
#     tom.pendown()


m = Turtle()

# for i in range(3):
#     m.color("black")
#     m.forward(100)
#     m.right(120)

# for i in range(4):
#     m.color("red")
#     m.forward(100)
#     m.right(90)

# for i in range(5):
#     m.color("blue")
#     m.forward(100)
#     m.right(72)

# for i in range(6):
#     m.color("dark goldenrod")
#     m.forward(100)
#     m.right(60)

# for i in range(7):
#     m.color("SeaGreen1")
#     m.forward(100)
#     m.right(51.428)
    
# for i in range(8):
#     m.color("cyan2")
#     m.forward(100)
#     m.right(45)
    

# for i in range(9):
#     m.color("khaki1")
#     m.forward(100)
#     m.right(40)
    
# for i in range(10):
#     m.color("green2")
#     m.forward(100)
#     m.right(36)

def draw_shape(num_side):
    for side in range(num_side):
        angle = 360/num_side
        m.forward(100)
        m.right(angle)

for shape_side in range(3,11):
    draw_shape(shape_side)

colors = []



screen = Screen()
screen.exitonclick()