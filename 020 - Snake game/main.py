from turtle import Screen
from snake import Snake
from food import Food
import random
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
food.appear()

screen.listen()
screen.onkey(key="w", fun=snake.turn_up)
screen.onkey(key="s", fun=snake.turn_down)
screen.onkey(key="a", fun=snake.turn_left)
screen.onkey(key="d", fun=snake.turn_right)
screen.onkey(key="c", fun=snake.new_segment)
screen.onkey(key="r", fun=food.appear)

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()

    snake.move()

screen.exitonclick()
