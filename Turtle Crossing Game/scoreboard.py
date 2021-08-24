from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-280, 260)
        self.write(arg=f"Level: {self.level}", font=FONT)

    def set_level(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT)

    def game_over_message(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)

