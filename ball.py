from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("#CDE8E5")
        self.goto(0, -150)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x_position = self.xcor() + self.x_move
        y_position = self.ycor() + self.y_move
        self.goto(x_position, y_position)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def level_up(self):
        self.move_speed *= 0.6

    def reset_position(self):
        self.goto(0, -150)
        self.y_move *= -1
