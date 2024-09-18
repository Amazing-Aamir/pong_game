from turtle import Turtle

class Score(Turtle):

    def __init__(self,position,player):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(position,240)
        self.player = player
        self.p1_score = 0
        self.p2_score = 0
        self.color('white')
        self.write(f"{self.player}   {self.p1_score}",align="center",font=('Arial',24,'normal'))

    def reset(self):
        self.clear()
        self.write(f"{self.player}   {self.p1_score}", align="center", font=('Arial', 24, 'normal'))

    def increase(self):
        self.p1_score += 1
        self.write(f"{self.player}  {self.p1_score}", align="center", font=('Arial', 24, 'normal'))
        self.reset()

    def gameover(self,win):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.color('white')
        self.write(f"Game Over!\n",align="center", font=('Arial', 32, 'normal'))
        self.write(f"{win} Won 🏆",align="center", font=('Arial', 32, 'normal'))
