import time
import turtle
from turtle import Screen
from square import Square
from ball import Ball
from block import Blocks
from score import Score
from lives import Lives

Screen().setup(width=800, height=600)
Screen().bgcolor("#686D76")
Screen().tracer(0)


def affichage_score(top_scr, actual_scr):
    final_score = turtle.Turtle()
    final_score.hideturtle()
    if int(top_scr["score"]) >= actual_scr:
        final_score.color("#FFDA78")
        final_score.write(f"The top score is {top_scr['score']}", False, "center", ("Arial", 28, "bold"))
    else:
        final_score.color("#ECB176")
        final_score.write(f"The new score is {actual_scr}", False, "center", ("Arial", 28, "bold"))


score = Score()
square = Square()
blocks = Blocks()
ball = Ball()
lives = Lives()

Screen().onkey(square.move_left, "Left")
Screen().onkey(square.move_right, "Right")

Screen().listen()

is_true = True

while is_true:
    time.sleep(ball.move_speed)
    Screen().update()
    ball.move()
    for block in blocks.all_blocs:
        if ball.distance(block) < 30:
            blocks.all_blocs.remove(block)
            if blocks.all_blocs:
                block.goto(500, 500)
                score.update_score()
                ball.bounce_y()
            else:
                ball.reset_position()
                ball.level_up()
                blocks.create_blocs()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.distance(square) < 30:
        ball.bounce_y()

    if ball.ycor() < -280:
        if lives.lives:
            ball.reset_position()
            lives.update_lives()
        else:
            top_score = score.show_score()
            affichage_score(top_score, score.score)
            is_true = False


Screen().exitonclick()
