from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segments(positions)

    def add_segments(self, positions):
        new_segment = Turtle(shape="square")
        new_segment.color("White")
        new_segment.penup()
        new_segment.goto(positions)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segments(self.segments[-1].pos())

    def move(self):
        for segm in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segm - 1].xcor()
            new_y = self.segments[segm - 1].ycor()
            self.segments[segm].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def left(self):
        angle = int(self.head.heading()) - 180
        if angle == 90 or angle == -90:
            self.head.setheading(180)

    def right(self):
        angle = int(self.head.heading()) - 360
        if angle == 90 or angle == -90 or angle == -270:
            self.head.setheading(0)

    def up(self):
        angle = int(self.head.heading()) - 90
        if angle == 90 or angle == -90:
            self.head.setheading(90)

    def down(self):
        angle = int(self.head.heading()) - 270
        if angle == 90 or angle == -90 or angle == -270:
            self.head.setheading(270)

