from turtle import Turtle, Screen
from snake import Snake
import time




screen =  Screen()
screen.setup(600,600) # game board size
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake = Snake()

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

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)
    snake.move()


screen.exitonclick()