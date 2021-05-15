from turtle import Turtle, Screen
import random

# Setup the screen
screen = Screen()
screen.setup(width=500, height=400)

# Setup the turtles
colors = ["red", "blue", "yellow", "black", "purple", "green"]
turtles = []
start_position = (-0.4 * screen.window_width(), 0.3 * screen.window_height())
space_between = 0.7 * screen.window_height() / len(colors)
end_position = 0.4 * screen.window_width()
for i in range(len(colors)):
    turtles.append(Turtle())
    turtles[i].shape("turtle")
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(start_position[0], start_position[1] - space_between * i)

# User guess
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color"
).lower()
while user_bet not in colors:
    user_bet = screen.textinput(
        title="Make your bet",
        prompt="Please input a valid color \nWhich turtle will win the race? Enter a color"
    ).lower()


def move_turtle(turtle):
    if random.randint(0, 1):
        turtle.forward(10)


def is_there_a_winner():
    for i in range(len(turtles)):
        if turtles[i].xcor() >= end_position:
            return i
    return -1


while is_there_a_winner() == -1:
    for i in range(len(turtles)):
        if is_there_a_winner() == -1:
            move_turtle(turtles[i])
        else:
            break

if user_bet == colors[is_there_a_winner()]:
    print(f"You won. The turtle winner is: {colors[is_there_a_winner()]} turtle")
else:
    print(f"You lose. The turtle winner is: {colors[is_there_a_winner()]} turtle")

screen.exitonclick()
