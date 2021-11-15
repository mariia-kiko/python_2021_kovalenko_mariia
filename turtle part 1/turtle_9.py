import turtle as t
import math

t.speed(10)
t.shape('turtle')

def polygon(n, r):
    for i in range(1, n+1, 1):
        t.forward(2*r*math.sin(math.pi/n))
        t.left(180 - (180*(n-2)/n))
                   
for j in range (3, 14, 1):
                   polygon(j, 15*j)
                   t.goto(-(2*15*(j+1)*math.sin(math.pi/(j+1)) - (2*15*j*math.sin(math.pi/j))), -(2*15*(j+1)*math.sin(math.pi/(j+1)) - (2*15*j*math.sin(math.pi/j))))
                   t.left(180 - (180*(j-2)/j))
                   
                   
