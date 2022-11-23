from turtle import Turtle, Screen
screen = Screen()


t = Turtle()

angle = 0


def forwards():
    t.forward(10)


def backwards():
    t.backward(10)


def clockwise():
    global angle
    angle -= 5
    t.setheading(angle)


def counterclockwise():
    global angle
    angle += 5
    t.setheading(angle)


def clear():
    t.reset()


screen.listen()
screen.onkey(fun=forwards, key="w")
screen.onkey(fun=backwards, key="s")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=counterclockwise, key="a")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
