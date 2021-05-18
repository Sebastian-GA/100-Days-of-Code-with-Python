from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        for i in range(3):
            self.segments.append(Turtle())
            self.segments[i].penup()
            self.segments[i].shape("square")
            self.segments[i].color("white")
            self.segments[i].goto(i * 20, 0)

        self.segments[0].setheading(180)

    def move(self):
        for i in range(1, len(self.segments)):
            i = -i
            new_position = self.segments[i - 1].pos()
            self.segments[i].goto(new_position)

        self.segments[0].forward(20)

    def turn_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def turn_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def turn_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def turn_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def new_segment(self):
        self.segments.insert(0, Turtle())
        self.segments[0].penup()
        self.segments[0].shape("square")
        self.segments[0].color("white")

        if self.segments[1].heading() == 0:
            self.segments[0].goto(self.segments[1].xcor() + 20, self.segments[1].ycor())
        elif self.segments[1].heading() == 90:
            self.segments[0].goto(self.segments[1].xcor(), self.segments[1].ycor() + 20)
        elif self.segments[1].heading() == 180:
            self.segments[0].goto(self.segments[1].xcor() - 20, self.segments[1].ycor())
        else:
            self.segments[0].goto(self.segments[1].xcor(), self.segments[1].ycor() - 20)

        self.segments[0].setheading(self.segments[1].heading())
