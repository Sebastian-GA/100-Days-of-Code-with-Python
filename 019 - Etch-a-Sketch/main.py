from turtle import Turtle, Screen

tom = Turtle()
tom.shape("classic")
screen = Screen()


def turn_left():
    tom.left(10)


def turn_right():
    tom.right(10)


def move_forward():
    tom.forward(10)


def move_backward():
    tom.backward(10)


def clear_screen():
    tom.hideturtle()
    tom.penup()
    tom.home()
    tom.showturtle()
    tom.pendown()
    tom.clear()


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
