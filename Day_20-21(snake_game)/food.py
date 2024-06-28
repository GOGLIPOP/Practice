from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)

        while x % 10 != 0 or y % 10 != 0:
            new_x = random.randint(-290, 290)
            x = new_x
            new_y = random.randint(-290, 290)
            y = new_y
        else:
            self.goto(x=x, y=y)
            # print(f"x = {x}, y = {y}")




