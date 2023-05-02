import math
import turtle


def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)


def circle():
    for i in range(72):
        turtle.forward(10)
        turtle.left(5)


def many_squares(number_of_squares=5):
    for i in range(1, number_of_squares + 1):
        square(i * 40)
        turtle.penup()
        turtle.goto(-i * 40 / 2, -i * 40 / 2)
        turtle.pendown()


def polygon(side_size=50, number_of_sides=4):
    for i in range(number_of_sides):
        turtle.forward(side_size)
        turtle.left(360 / number_of_sides)


def spider(number_of_legs, legs_size=100):
    for i in range(number_of_legs):
        turtle.forward(legs_size)
        turtle.left(180)
        turtle.forward(legs_size)
        turtle.left(180)
        turtle.left(360 / number_of_legs)


def spiral(step=5, number_of_points=250):
    alpha = 0
    for i in range(number_of_points):
        alpha += 0.1
        r = alpha * step
        x = r * math.cos(alpha)
        y = r * math.sin(alpha)
        turtle.goto(x, y)


for i in range(9):
    print(i)
