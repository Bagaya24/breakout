from turtle import Turtle
from random import choice

colors = ["#7469B6", "#FEEFAD", "#68D2E8", "#FF0000", "#987070", "#DC5F00", "#FFE8C8", "#028391", "#850F8D", "#003285",
          "#A1DD70", "#ECB176", "#FFDA78"]


class Blocks:
    def __init__(self):
        super().__init__()
        self.all_blocs = []
        self.create_blocs()

    def create_blocs(self):
        for i in range(50, 250, 30):
            for j in range(-360, 400, 60):
                new_bloc = Turtle()
                new_bloc.shape("square")
                new_bloc.speed(10)
                new_bloc.color(choice(colors))
                new_bloc.penup()
                new_bloc.shapesize(1, 3)
                new_bloc.goto(j, i)
                self.all_blocs.append(new_bloc)
