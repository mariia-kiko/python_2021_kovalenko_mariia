import turtle
import math

turtle.shape('turtle')

def circle1(r, n):
    for i in range(n):
        turtle.left(180 - ((n - 2)*180/n))
        turtle.forward(r*math.sin(math.pi/n))
        
def circle2(r, n):
    for i in range(n):
        turtle.right(180 - ((n - 2)*180/n)) 
        turtle.forward(r*math.sin(math.pi/n))
        
for j in range (1, 10, 1):
        circle1(10*j + 30,100)
        circle2(10*j + 30,100)
                       
