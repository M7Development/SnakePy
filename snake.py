from turtle import Turtle

#holder = []
#for i in range(2):
#    new_ = Turtle(i)
#    holder.append(new_)
#
#print(holder)

new_turtle = Turtle()
new_turtle1 = Turtle()
new_turtle2 = Turtle()

new_turtle.penup()
new_turtle1.penup()
new_turtle2.penup()

startSnake = []
fragmentData = [
    {"turtle": new_turtle, "color": new_turtle.color("white"), "shape": new_turtle.shape("square"), "position": new_turtle.goto(x=0, y=0)},
    {"turtle": new_turtle1, "color": new_turtle1.color("white"), "shape": new_turtle1.shape("square"), "position": new_turtle1.goto(x=-20, y=0)},
    {"turtle": new_turtle2, "color": new_turtle2.color("white"), "shape": new_turtle2.shape("square"), "position": new_turtle2.goto(x=-40, y=0)}
]


class Snake:

    def __init__(self, listsnake):
        self.listsnake = listsnake

    def listerweiterung(self, erweiterung):
        self.listsnake = erweiterung

    def leftTurn(self):
        self.listsnake[0].turtle.left(90)

    def rightTurn(self):
        self.listsnake[0].turtle.right(90)


class Fragment:

    def __init__(self, turtle, color, shape, position):
        self.turtle = turtle
        self.color = color
        self.shape = shape
        self.position = position
