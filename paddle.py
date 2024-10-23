from turtle import Turtle

SPEED = 50
DOWN = 20
UP = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_len=1, stretch_wid=6)
        self.penup()
        if position == "left":
            self.goto(-350, 0)
        else:
            self.goto(350, 0)
        self.speed(SPEED)

    def move_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - DOWN
            self.goto(self.xcor(), new_y)

    def move_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + UP
            self.goto(self.xcor(), new_y)
