from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# din screen bör vara rektanguljär, ex. 800x600


def main():
    """Summary: Screen is imported from turtle. This creates the base.
    Adds and title to the turtle screen and mesurments of the size

    value: screen = Screen()

    This connects everything together
    """
    screen = Screen()
    screen.setup(800, 600)
    screen.bgcolor("black")
    screen.title("Pong game:")
    screen.tracer(0)

    """_summary_ : While the game_is_on is equaled to true, it regiestera all thoes values. 
        Impletend all classes from it's own file with new object.
        For example, paddle_a = Paddle("left"); This brings all the elements and commands from paddle file as paddle

        Value: ball, paddle_a/b, scoreboard
    """
    game_is_on = True
    paddle_a = Paddle("left")
    paddle_b = Paddle("right")
    ball = Ball()
    scoreboard = Scoreboard()

    # Move the paddels up and down in the y-cordinate
    # This thorugh asigned key's to click on, in order for it to move: "w", "s" Which is fixed to left_player.
    # Value: screen.listen(), Onkey: This makes the paddels work

    screen.listen()
    screen.onkey(paddle_a.move_up, "w")
    screen.onkey(paddle_a.move_down, "s")
    screen.onkey(paddle_b.move_up, "Up")
    screen.onkey(paddle_b.move_down, "Down")

    # Make the game run with game_is_on due to it being = True.
    # Puts on a time tracer which gives a little pause before it starts.
    while game_is_on:
        time.sleep(0.05)
        screen.update()
        ball.move()  # Call on the function move() from the ball.py. There it register the code written there
        # code below make the ball bounce when it hits the paddles.
        if (ball.xcor() > 320 and ball.distance(paddle_b) < 50) or (
            ball.xcor() < -320 and ball.distance(paddle_a) < 50
        ):
            ball.bounce_x()

        if ball.xcor() > 380:
            ball.reset()
            scoreboard.left_player()

        if ball.xcor() < -380:
            ball.reset()
            scoreboard.right_player()

    screen.exitonclick()  # When clicking the user should exit the program


if __name__ == "__main__":
    main()
