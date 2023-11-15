"""This is the turtle tutorial."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.penup()
leo.goto(-120,0)
leo.pendown()
leo.color("blue")
leo.fillcolor("blue")
leo.begin_fill()
leo.end_fill()
idx: int = 0
while idx < 3:
    leo.forward(300)
    leo.left(120)
    idx += 1