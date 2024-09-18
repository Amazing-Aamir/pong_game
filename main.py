from turtle import Screen
from score import Score
from paddle import Paddle
from ball import Ball
import time


scr = Screen()
scr.setup(800,600)
scr.title('Pong')
scr.bgcolor('black')
scr.tracer(0)
player1 = scr.textinput("Player1", "Enter your name").capitalize()
player2 = scr.textinput("Player2", "Enter your name").capitalize()
point_to_win = scr.textinput("Point to win", "How many points to win")
win = int(point_to_win)
p1_score = 0
p2_score = 0
ball_speed = 0.1
paddle_collide = 0

r_paddle = Paddle(360)
l_paddle = Paddle(-360)
ball = Ball()
score_r = Score(200,player1)
score_l = Score(-200,player2)

scr.listen()
scr.onkeypress(fun=r_paddle.paddle_up, key='Up')
scr.onkeypress(fun=r_paddle.paddle_down, key='Down')
scr.onkeypress(fun=l_paddle.paddle_up, key='w')
scr.onkeypress(fun=l_paddle.paddle_down, key='s')

game_is_on = True

while game_is_on:
    time.sleep(ball_speed)
    scr.update()
    ball.move()
    print(ball_speed)

    if ball.ycor() > 240 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r_paddle) < 50  and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.x_bounce()
        paddle_collide += 1


    if ball.xcor() == 400:
        p2_score += 1
        score_l.increase()
        ball.reset()
    elif ball.xcor() == -400:
        p1_score += 1
        score_r.increase()
        ball.reset()

    if paddle_collide == 6:
        if ball_speed > 0.030000000000000013:
            ball_speed -= 0.01
            paddle_collide = 0

    if p1_score == win or p2_score == win:
        game_is_on = False
        if p1_score > p2_score:
            score_r.gameover(player1)
        else:
            score_l.gameover(player2)



scr.exitonclick()