"""This is the turtle project."""
__author__ = "730669473"
from turtle import Turtle, colormode, done 
colormode(255)

turtle: Turtle = Turtle()
radius: int = 200


def main() -> None:
    """The entry point of the scene."""
    turtle.speed(0)
    first(turtle, -120, 50, 400)
    second(turtle, 150, 30, 100)
    third(turtle, 0, -100, 200)
    fourth(turtle, 0, -100, 200)
    fourth(turtle, 60, -20, 200)
    fourth(turtle, -90, -20, 200)
    
    done()


def first(turtle: Turtle, x: float, y: float, width: float) -> None:
    """Going to draw the first part of my art, which is a take on a star."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("blue")
    turtle.fillcolor("blue")
    turtle.begin_fill()
    idx: int = 0
    while idx < 5:
        turtle.forward(width)
        turtle.left(200)
        idx += 1
    turtle.end_fill()


def second(turtle: Turtle, z: float, v: float, width: float) -> None:
    """Second part of the drawing, putting it at the base of the star in a sun shape."""
    turtle.penup()
    turtle.goto(z, v)
    turtle.pendown()
    turtle.color("red")
    turtle.fillcolor("red")
    turtle.begin_fill()
    idx: int = 0
    while idx < 20:
        turtle.forward(width)
        turtle.right(100)
        idx += 1
    turtle.end_fill()


def third(turtle: Turtle, z: float, v: float, width: float) -> None:
    """Third shpae in my drawing and is a smiley face."""
    turtle.penup()
    turtle.goto(z, v)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.goto(z - 100, v + 100)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(radius - 175)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(z - 250, v + 100)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(radius - 175)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(z - 230, v - 40)
    turtle.pendown()
    turtle.right(178)
    turtle.circle(40, 190)
    turtle.penup()
    turtle.goto(z, v)
    
    
def fourth(turtle: Turtle, z: float, v: float, width: float) -> None:
    """Going to add a nose to my smiley face."""
    turtle.penup()
    turtle.goto(z - 175, v + 20)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(radius - 190)
    turtle.end_fill()


if __name__ == "__main__":
    main()