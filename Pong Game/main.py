from turtle import Screen
from paddles import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

ball = Ball()

score = Scoreboard()

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-pong")
screen.tracer(0)


screen.listen()
screen.onkeypress(left_paddle.up, "Up")
screen.onkeypress(left_paddle.down, "Down")
screen.onkeypress(right_paddle.up, "w")
screen.onkeypress(right_paddle.down, "s")

game_on = True
while game_on:

    time.sleep(ball.velocidade)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_paddle()
        score.add_point_right()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
        score.add_point_left()

    # detect if paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        score.add_point_left()

    if ball.xcor() < -380:
        ball.reset_position()
        score.add_point_right()


screen.exitonclick()