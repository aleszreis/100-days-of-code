from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_points = 0
        self.r_points = 0
        self.set_score()

    def set_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_points, move=False, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(arg=self.r_points, move=False, align=ALIGNMENT, font=FONT)

    def add_point_left(self):
        self.l_points += 1
        self.set_score()

    def add_point_right(self):
        self.r_points += 1
        self.set_score()
