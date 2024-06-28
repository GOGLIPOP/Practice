from turtle import Turtle
import datetime


time = datetime.datetime.now().strftime("%d-%m-%Y %X")
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "a+") as my_file:
            ...
        with open("data.txt", "r") as my_file:
            self.old_score = my_file.read()
            try:
                self.old_score = str(self.old_score[-1])
            except IndexError:
                ...
            if my_file.tell() == 0:
                with open("data.txt", "w") as my_file:
                    my_file.write(str(f"{time} - {0}"))

        self.penup()
        self.color("white")
        self.hideturtle()
        self.setpos(x=10, y=260)
        if self.old_score:
            self.write(arg=f"Score: {self.score}  High Score: {self.old_score}", move=False, font=FONT, align="center")
        else:
            self.write(arg=f"Score: {self.score}", move=False, font=FONT, align="center")

    def increase_score(self):
        self.score += 1
        self.clear()
        if self.old_score:
            self.write(arg=f"Score: {self.score}  High Score: {self.old_score}", move=False, font=FONT, align="center")
        else:
            self.write(arg=f"Score: {self.score}", move=False, font=FONT, align="center")

    def game_over(self):
        self.clear()
        self.write(arg=f"GAME OVER", move=False, font=FONT, align="center")
        try:
            if self.score > int(self.old_score[-1]):
                with open("data.txt", "w") as my_file:
                    my_file.write(str(f"{time} - {self.score}"))
        except IndexError:
                with open("data.txt", "w") as my_file:
                    my_file.write(str(f"{time} - {self.score}"))
