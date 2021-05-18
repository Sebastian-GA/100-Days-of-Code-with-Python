from turtle import Screen
from snake import Snake
from food import Food
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

# Snake and food settings
snake = Snake()
food = Food(screen_width=screen.window_width(), screen_height=screen.window_height())


def is_food_in_contact_with_snake():
    for i in range(len(snake.segments)):
        if snake.segments[i].distance(food) < 10:
            print("touching")
            return [i, True]
    return [0, False]


# Reappear food if is in contact with the snake
while is_food_in_contact_with_snake()[1]:
    food.appear()

# Keys settings
screen.listen()
screen.onkey(key="w", fun=snake.turn_up)
screen.onkey(key="s", fun=snake.turn_down)
screen.onkey(key="a", fun=snake.turn_left)
screen.onkey(key="d", fun=snake.turn_right)
screen.onkey(key="c", fun=snake.new_segment)
screen.onkey(key="r", fun=food.appear)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    # Detecting if collision with food
    if is_food_in_contact_with_snake() == [0, True]:
        snake.new_segment()
        while is_food_in_contact_with_snake()[1]:
            food.appear()
    
screen.exitonclick()
