from turtle import Turtle, colormode, done

colormode(255)
leo: Turtle = Turtle()
#3rd line contrusts a new Turtle object your program will control"""


"""leo.penup()
leo.goto(-130, -80)
leo.pendown()
#where to place the turtle (think of coordinate planes)

leo.color(255, 192, 253) 
#color of fill + outline of shape

leo.speed(10)
leo.hideturtle()
#speed of fill and hiding turtle 

leo.begin_fill()
"""
side_length: int = 850

""""i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i = i + 1
leo.end_fill()"""

bob: Turtle = Turtle()
#bob.screen.bgcolor('blue')
bob.penup()
bob.hideturtle()
bob.goto(-70, 120)
bob.pencolor(0, 0, 0)
bob.fillcolor()
bob.pendown()
bob.speed(5)

bob.left(210)
bob.begin_fill()
bob.circle(120, 300)
bob.goto(-70,120)
bob.end_fill()

done()

"""leo.pencolor("pink")
    leo.fillcolor(32, 67, 93)
    leo.color("green", "yellow")
    3rd line is <turtlevariable>.color(<pencolor>, <fillcolor>) format
"""