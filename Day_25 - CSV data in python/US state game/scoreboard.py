from turtle import Turtle
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self, x, y, state_name):
        # self.x = x
        # self.y = y
        self.goto(x, y)
        self.write(f"{state_name}", align=ALIGNMENT)
