import turtle
import math
turtle.shape('turtle')
def circle1 (r):
    for i in range(10*r):
        turtle.forward(200*math.sin(math.pi/(10*r)))
        turtle.left(180 - ((10*r -2)*180/(10*r)))
def circle2 (r):
    for i in range(10*r):
        turtle.forward(200*math.sin(math.pi/(10*r)))
        turtle.right(180 - ((10*r -2)*180/(10*r)))
circle1(5)
circle2(5)
turtle.left(120)
circle1(5)
circle2(5)
turtle.left(120)
circle1(5)
circle2(5)
turtle.left(120)

