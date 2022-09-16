from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(300, random.randint(-280, 280))
        self.setheading(180)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.current_speed = STARTING_MOVE_DISTANCE

    def move_car(self):
        if self.xcor() >= -280:
            self.forward(self.current_speed)
        else:
            self.goto(280, self.ycor())

    def level_up(self):
        self.current_speed += MOVE_INCREMENT

