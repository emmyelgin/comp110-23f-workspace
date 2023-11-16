"""Turtle Tutorial."""

__author__ = "730464992"

from turtle import Turtle, done


def position_turtle(turtle: Turtle, x: float, y: float, rotation: float) -> None:
    """Reset cursor position to draw in global space."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown() 
    turtle.setheading(0)
    turtle.left(rotation)


def draw_rectangle(turtle: Turtle, x: float, y: float, width: float, height: float, rotation: float) -> None:
    """Draw rectangle shape."""
    position_turtle(turtle, x, y, rotation)
    i: int = 0
    while (i < 4):
        if i % 2 == 0:
            turtle.forward(width)
        else:
            turtle.forward(height)
        i = i + 1
        turtle.left(90)


def draw_eq_triangle(turtle: Turtle, x: float, y: float, side: float, rotation: float) -> None:
    """Draw equilateral triangle."""
    position_turtle(turtle, x, y, rotation)
    i: int = 0
    while (i < 3):
        turtle.forward(side)
        i = i + 1
        turtle.left(120)


def draw_circle(turtle: Turtle, x: float, y: float, number_of_sides: float, side_length: float, rotation: float) -> None: 
    """Draw approximated circle."""
    position_turtle(turtle, x, y, rotation)
    i: int = 0
    while (i < number_of_sides):
        turtle.forward(side_length)
        i = i + 1
        turtle.left(360 / number_of_sides)


def draw_spiral(turtle: Turtle, x: float, y: float, angle: float, delta_angle: float, side: float, delta_side: float, turns: int, rotation: float) -> None:
    """Draw spiral with changing side and angle."""
    position_turtle(turtle, x, y, rotation)
    i: int = 0
    while (i < turns):
        turtle.forward(side)
        turtle.left(angle)
        i = i + 1
        side = side + delta_side
        angle = angle + delta_angle 
 

def main() -> None: 
    """Entry point of my scene."""
    leo: Turtle = Turtle()
    draw_spiral(leo, 60, 40, 30, +5, 50, -2, 20, 0)
    leo.begin_fill()
    draw_spiral(leo, -80, -60, 50, 4, 80, 20, 10, 0)
    leo.end_fill()
    draw_rectangle(leo, -20, -50, 40, 60, 0)
    leo.color("red")
    draw_eq_triangle(leo, 120, 170, 50, 0)
    leo.color("blue")
    leo.begin_fill()
    draw_circle(leo, -150, -30, 100, 2, 0)
    leo.end_fill()
    done()


if __name__ == "__main__": 
    main()