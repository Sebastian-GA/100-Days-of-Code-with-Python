from turtle import Turtle


class Segment(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.penup()
        # self.shapesize(0.9)


class Snake:
    def __init__(self):
        self.segments = []
        for i in range(3):
            self.segments.append(Segment())
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

    def extend(self):
        position = self.segments[-1].position()
        self.segments.append(Segment())
        self.segments[-1].goto(position)

    def is_colling_itself(self):
        for i in range(1, len(self.segments)):
            if self.segments[0].distance(self.segments[i]) < 15:
                return True
        return False
