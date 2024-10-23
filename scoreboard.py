from turtle import Turtle
from tkinter import CENTER

ALIGNMENT = CENTER
FONT = ("Courier", 24, "normal")
POSITION = (0, 265)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Blue")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()  # Update the previous scoreboard
        self.goto(-200, 260)
        self.write(f"Left_player:{self.left_score}", align="center", font=FONT)
        self.goto(200, 260)
        self.write(f"Right_player:{self.right_score}", align="center", font=FONT)

    def left_player(self):
        self.left_score += 1
        self.update_score()

    def right_player(self):
        self.right_score += 1
        self.update_score()
