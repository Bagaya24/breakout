from turtle import Turtle


class Square(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 4)
        self.color("#153448")
        self.speed(10)
        self.penup()
        self.goto(x=0, y=-200)

    def move_left(self):
        self.bk(30)

    def move_right(self):
        self.fd(30)
