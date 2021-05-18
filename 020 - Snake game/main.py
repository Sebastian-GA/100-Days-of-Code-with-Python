from turtle import Turtle, Screen
import random
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

# Snake setup
snake = []
for i in range(3):
    snake.append(Turtle())
    snake[i].penup()
    snake[i].shape("square")
    snake[i].color("white")
    snake[i].goto(i*20, 0)

snake[0].setheading(180)
snake[0].color("yellow")
snake[1].color("blue")
snake[2].color("green")


def update_body():
    for i in range(1, len(snake)):
        i = -i
        new_position = snake[i-1].pos()
        snake[i].goto(new_position)

    snake[0].forward(20)


def move_left():
    snake[0].setheading(180)


def move_right():
    snake[0].setheading(0)


def move_up():
    snake[0].setheading(90)


def move_down():
    snake[0].setheading(270)


def new_segment():
    snake.insert(0, Turtle())
    snake[0].penup()
    snake[0].shape("square")
    snake[0].color("white")
    if snake[1].heading() == 0:
        snake[0].goto(snake[1].xcor() +20, snake[1].ycor())
    elif snake[1].heading() == 90:
        snake[0].goto(snake[1].xcor(), snake[1].ycor() +20)
    elif snake[1].heading() == 180:
        snake[0].goto(snake[1].xcor() -20, snake[1].ycor())
    else:
        snake[0].goto(snake[1].xcor(), snake[1].ycor() -20)

    snake[0].setheading(snake[1].heading())


game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()

    screen.listen()
    screen.onkey(key="w", fun=move_up)
    screen.onkey(key="s", fun=move_down)
    screen.onkey(key="a", fun=move_left)
    screen.onkey(key="d", fun=move_right)
    screen.onkey(key="c", fun=new_segment)

    update_body()

screen.exitonclick()
