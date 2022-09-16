from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()  # No need to draw a line when positioning the score
        self.hideturtle()  # No need to show the turtle
        self.goto(-280, 260)
        self.print_scoreboard()

    def level_up(self):
        self.level += 1
        self.print_scoreboard()

    def print_scoreboard(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", move=False, font=FONT)
