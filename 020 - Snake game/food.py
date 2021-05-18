from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("violet")
        self.shape("square")
        self.shapesize(0.5)

    def appear(self):
        xcor = random.randint(-300 + 40, 300 - 40)
        ycor = random.randint(-300 + 40, 300 - 40)
        while xcor % 20 != 0:
            xcor = random.randint(-300 + 40, 300 - 40)
        while ycor % 20 != 0:
            ycor = random.randint(-300 + 40, 300 - 40)

        self.goto((xcor, ycor))
