from turtle import Screen
from class_snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

game_is_on = True


def file_func():
    with open("score.txt", "r") as my_file:
        my_file.write(scoreboard.score)


screen = Screen()
screen.setup(width=600, height=600)
screen.title("My snake game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    x = abs(int(snake.head.xcor()))
    y = abs(int(snake.head.ycor()))

    if x >= 300 or y >= 300:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[2:0]:
        if segment == snake.head:
            ...
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

screen.exitonclick()
