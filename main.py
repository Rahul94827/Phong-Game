from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Phong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

flag = True
while flag:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move_ball()

    # Detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting collision with the wall
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    #Detect right paddle misses the ball
    if ball.xcor()>380:
        ball.reset_pos()
        scoreboard.l_point()

    if ball.xcor()<-380:
        ball.reset_pos()
        scoreboard.r_point()

screen.exitonclick()
