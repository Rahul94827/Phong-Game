from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.width = 20
        self.height = 20
        self.x_mov = 10
        self.y_mov = 10
        self.ball_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_mov
        new_y = self.ycor() + self.y_mov
        self.penup()
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_mov *= -1

    def bounce_x(self):
        self.x_mov *= -1
        self.ball_speed *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
