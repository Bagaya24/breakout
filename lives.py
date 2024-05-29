import turtle


class Lives:
    def __init__(self):
        self.lives = 3
        self.turtle_lives = turtle.Turtle()
        self.turtle_lives.penup()
        self.turtle_lives.goto(-370, 260)
        self.turtle_lives.color("#EE4E4E")
        self.turtle_lives.hideturtle()
        self.update_lives()

    def update_lives(self):
        self.turtle_lives.clear()
        self.turtle_lives.write(self.lives * "❤️", False, "left", ("", 24, ""))
        self.lives -= 1
