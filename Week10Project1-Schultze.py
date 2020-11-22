from turtle import *

def drawCircle(t, x, y, radius):
    """Draws a circle using turtle t, with origin at x, y, with a specified radius"""
    t.up()
    t.goto(x, y - radius)
    t.down()
    for count in range(120):
        distance = (2.0 * 3.14 * radius )/ 120.0
        t.left(3)
        t.forward(distance)
