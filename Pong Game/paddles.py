from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x, y)


    def up(self):
        if self.ycor() < 250:
            y = self.ycor()
            self.goto(self.xcor(), y + MOVE_DISTANCE)

    def down(self):
        if self.ycor() > -250:
            y = self.ycor()
            self.goto(self.xcor(), y - MOVE_DISTANCE)


