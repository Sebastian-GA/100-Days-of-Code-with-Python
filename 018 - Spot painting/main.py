import turtle
from turtle import Turtle, Screen
import random
import colorgram


# Extract the colors of the image
colors = colorgram.extract("spots.jpg", 10)
for i in range(len(colors)):
    colors[i] = colors[i].rgb

# Setup the turtle
turtle.colormode(255)
tommy = Turtle()
tommy.speed(10)
tommy.hideturtle()

# Setup the art parameters
art_size = 10
dot_size = 30
space_between_dots = dot_size * 1.5
# set the new origin to draw the picture in the center
new_origin = - (- 0.5 + art_size / 2) * space_between_dots

for y in range(art_size):
    for x in range(art_size):
        tommy.penup()
        tommy.goto(new_origin + x * space_between_dots, new_origin + y * space_between_dots)
        tommy.pendown()
        color = random.choice(colors)
        tommy.dot(dot_size, color)

screen = Screen()
screen.exitonclick()
