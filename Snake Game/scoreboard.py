from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.points = 0
        with open("data.txt") as file:
            self.higher_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.points} High Score: {self.higher_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.points += 1
        self.update_scoreboard()

    def reset(self):
        if self.points > self.higher_score:
            self.higher_score = self.points
            with open("data.txt", mode="w") as file:
                file.write(f"{self.higher_score}")
        self.points = 0
        self.update_scoreboard()
