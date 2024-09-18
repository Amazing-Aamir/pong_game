from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,x_axis):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(x_axis,0)

    def paddle_up(self):
        if self.ycor() != 240:
            y_axis = self.ycor() + 20
            self.goto(self.xcor(), y_axis)

    def paddle_down(self):
        if self.ycor() != -240:
            y_axis = self.ycor() - 20
            self.goto(self.xcor(), y_axis)

