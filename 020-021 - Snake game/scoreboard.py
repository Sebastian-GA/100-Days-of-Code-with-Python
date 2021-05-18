from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.score = 0
        self.location = (0, screen_height / 2 - 20)
        self.font = "Consolas"
        self.text_size = 15
        self.text_style = "normal"
        self.text_format = (self.font, self.text_size, self.text_style)
        self.settings()
        self.speed("fastest")

    def settings(self):
        self.reset()
        self.hideturtle()
        self.penup()
        self.goto(self.location)
        self.pencolor("white")
        self.text_format = (self.font, self.text_size, self.text_style)

    def print_score(self):
        self.settings()
        text = f"Score: {self.score}"
        self.write(arg=text, font=self.text_format, align="center")

    def game_over(self):
        self.goto(0, 0)
        text = "GAME OVER"
        self.write(arg=text, font=self.text_format, align="center")

    def reset_score(self):
        self.score = 0

    def increase(self):
        self.score += 1
