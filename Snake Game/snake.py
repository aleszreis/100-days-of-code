from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.size = []
        self.create()
        self.head = self.size[0]

    def create(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.size.append(new_segment)

    def extend(self):
        self.add_segment(self.size[-1].position())

    def move(self):
        for i in range(len(self.size) - 1, 0, -1):
            new_x = self.size[i - 1].xcor()
            new_y = self.size[i - 1].ycor()
            self.size[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for i in self.size:
            i.goto(2000, 2000)
        self.size.clear()
        self.create()
        self.head = self.size[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)