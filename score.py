import turtle
import json

class Score:
    def __init__(self):
        self.score = 0
        self.tout_score = {}
        self.turtle_score = turtle.Turtle()
        self.turtle_score.penup()
        self.turtle_score.goto(310, 260)
        self.turtle_score.color("white")
        self.turtle_score.hideturtle()
        self.turtle_score.write(f"Score: {self.score} ", False, "center", ("Arial", 20, "normal"))

    def update_score(self):
        self.turtle_score.clear()
        self.score += 1
        self.turtle_score.write(f"Score: {self.score} ", False, "center", ("Arial", 20, "normal"))


    def enregistrement_score(self):
        with open("./data/score.json", "r") as file:
            data = json.load(file)
            self.tout_score[f"score"] = self.score
            data.update(dict(self.tout_score))

        with open("./data/score.json", "w") as file:
            json.dump(data, file, indent=4, sort_keys=True)

    @staticmethod
    def show_score():
        with open("./data/score.json") as file:
            return json.load(file)
