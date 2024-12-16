from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.goto(0, 0)
        self.dx = 10
        self.dy = 10
        self.move_speed = 0.05

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

        if self.ycor() > 280:
            self.sety(280)
            self.bounce_y()

        elif self.ycor() < -280:
            self.sety(-280)
            self.bounce_y()

    def reset(self) -> None:
        self.goto(0, 0)
        self.speed = 0.05
        self.bounce_x()

    def bounce_x(self):
        self.dx *= -1

    def bounce_y(self):
        self.dy *= -1  # Bounce on the celling and changes dierection,
        self.move_speed *= (
            0.9  # another feature is to build up it's speed(momentum) with move_speed
        )
