import turtle as t
import math

t.speed(10)
t.shape('turtle')

t.left(90)
t.penup()
t.goto(-150, 0)
t.pendown()

def arc(r):
  for i in range(30):
    t.fd(r * math.pi/60)
    t.right(6)

def spring(n):
  for i in range(n):
    arc(90)
    arc(30)

spring(5)
