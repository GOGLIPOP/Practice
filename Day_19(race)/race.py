import random
from turtle import Turtle, Screen
import time


def display_message(message, color):
    time.sleep(2)
    screen.clearscreen()
    screen.bgcolor("white")
    message_turtle = Turtle()
    message_turtle.hideturtle()
    message_turtle.penup()
    message_turtle.color(color)
    message_turtle.goto(0, 0)
    message_turtle.write(message, align="center", font=("Arial", 18, "normal"))


is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="How will win the race? Enter a color\n"
                                                          "(red, orange, dark blue, green, purple, blue, yellow)").lower()

colors = ["red", "orange", "dark blue", "green", "purple", "blue", "yellow"]
y_poz = [-70, -40, -10, 20, 50, 80, 110]
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_poz[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if int(turtle.pos()[0]) >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                display_message(f"You've won! The {winning_color} turtle is the winner!", "green")
            else:
                display_message(f"You've lost! The {winning_color} turtle is the winner!", "red")
            break
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
