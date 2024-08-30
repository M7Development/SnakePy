from turtle import Screen, Turtle
import time

import controller
from snake import fragmentData, Fragment, Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake([])
snake.listerweiterung(controller.basisSnake())

screen.update()

game_is_on = True

screen.listen()
#while game_is_on:
#    screen.onkey(key="a", fun=snake.leftTurn)
#    screen.onkey(key="s", fun=snake.rightTurn)
#    screen.update()
#    time.sleep(0.1)
#    for at in range(len(snake.listsnake) - 1, -1, -1):
#        if at == 0:
#            snake.listsnake[at].turtle.speed(1)
#            snake.listsnake[at].turtle.forward(20)
#        else:
#            new_x = snake.listsnake[at - 1].turtle.xcor()
#            print(new_x)
#            new_y = snake.listsnake[at - 1].turtle.ycor()
#            print(new_y)
#            snake.listsnake[at].turtle.goto(new_x, new_y)

screen.exitonclick()
