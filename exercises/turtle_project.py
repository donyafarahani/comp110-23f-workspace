"""My artpeice portrays 3 circular, neon-colored fish swimming in a fish bowl that is floating in the middle of a open ocean on a very starry night."""

__author__ = "730661618"

from turtle import Turtle, colormode, done
from random import randint


def draw_bowl(a_turtle: Turtle, x: float, y: float) -> None:
    """This function draws a fish bowl. The bowl's bottom corner is located at x, y, and it is then rotated left 210 degrees to appear in the center of the scene."""
    a_turtle.penup()
    a_turtle.speed(0)
    a_turtle.goto(-70, 120)
    a_turtle.pencolor(255, 255, 255)
    a_turtle.fillcolor(105, 129, 193)
    a_turtle.pendown()
    a_turtle.left(210)
    
    a_turtle.begin_fill()
    a_turtle.circle(x, y)
    a_turtle.goto(-70, x)
    a_turtle.end_fill()


def draw_water(a_turtle: Turtle, x: float, y: float, side_length: float) -> None:
    """This function draws a rectangle for the ocean's water with a given side length, and where the bottom-left of the rectangle is at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()

    a_turtle.fillcolor(46, 72, 142) 
    a_turtle.begin_fill()
    a_turtle.speed(0)
    
    i: int = 0
    while (i < 4):
        if i % 2 == 0:
            a_turtle.forward(side_length)
            a_turtle.left(90)
        else:
            a_turtle.forward(side_length / 2)
            a_turtle.left(90)
        i = i + 1
    a_turtle.end_fill()


def draw_fish(a_turtle: Turtle, x: float, y: float) -> None:
    """This function draws 3 circle-sized fish inside the fish bowl, where x, y is the position that the circle begins."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.fillcolor(232, 6, 253)
    a_turtle.pendown()
    a_turtle.speed(0)
    a_turtle.begin_fill()
    a_turtle.circle(10)
    a_turtle.end_fill()

    x += 65.0
    y += 40.0

    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.fillcolor(6, 253, 240)
    a_turtle.pendown()
    a_turtle.speed(0)
    a_turtle.begin_fill()
    a_turtle.circle(10)
    a_turtle.end_fill()

    x += 50.0
    y -= 90.0

    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.fillcolor(10, 231, 5)
    a_turtle.pendown()
    a_turtle.speed(0)
    a_turtle.begin_fill()
    a_turtle.circle(10)
    a_turtle.end_fill()

    
def draw_sky(a_turtle: Turtle, x: float, y: float, side_length: float) -> None:
    """This function draws a rectangular sky with a given side length, and where the top-left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()

    a_turtle.fillcolor(8, 28, 79) 
    a_turtle.begin_fill()
    a_turtle.speed(0)
    
    i: int = 0
    while (i < 4):
        if i % 2 == 0:
            a_turtle.forward(side_length)
            a_turtle.right(90)
        else:
            a_turtle.forward(side_length / 2)
            a_turtle.right(90)
        i = i + 1
    a_turtle.end_fill()


def draw_stars(a_turtle: Turtle, x: float, y: float, side_length: float, num: int) -> None:
    """This function draws triangular stars of the given sizeand the bottom-left corner is located at x, y."""
    a_turtle.speed(0)
    a_turtle.fillcolor(227, 230, 237) 
    
    for s in range(num):
        i: int = 0
        a_turtle.penup()
        a_turtle.goto(x, y)
        a_turtle.pendown()
        a_turtle.begin_fill()
        while (i < 3):
            a_turtle.forward(side_length)
            a_turtle.left(120)
            i = i + 1
        a_turtle.end_fill()
        x = randint(-350, 350)
        y = randint(150, 350)


def main() -> None:
    """The entrypoint of my scene."""
    colormode(255)
    bowl: Turtle = Turtle()
    fish: Turtle = Turtle()
    water: Turtle = Turtle()
    sky: Turtle = Turtle()
    star: Turtle = Turtle()

    bowl.hideturtle()
    fish.hideturtle()
    water.hideturtle()
    sky.hideturtle()
    star.hideturtle()
    
    # TODO: Declare your Turtle variable(s) here.
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.

    draw_water(water, -420, -375, 850)
    draw_sky(sky, -420, 473, 850)
    draw_bowl(bowl, 120, 300)
    draw_fish(fish, -50, 20)
    draw_stars(star, -300, 220, 15, 9)
    draw_stars(star, -300, 220, 30, 7)

    done()


# TODO: Use the __name__ is "__main__" idiom shown in class
if __name__ == "__main__":
    main()