from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.penup()
        self.color("violet")
        self.shape("square")
        self.shapesize(0.5)
        self.speed("fastest")
        self.screen_size = (screen_width, screen_height)
        self.appear()

    def appear(self):
        position = (self.screen_size[0] // 2) // 20
        position -= 1
        xcor = random.randint(-position, position) * 20
        ycor = random.randint(-position, position) * 20

        self.goto((xcor, ycor))
