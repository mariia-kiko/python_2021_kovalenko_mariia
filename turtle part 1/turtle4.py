import turtle as t
import math

t.speed(15)
t.shape('turtle')

for i in range(1000):
    t.forward(200*math.sin(math.pi/1000))
    t.left(180 - (998*180/1000))
