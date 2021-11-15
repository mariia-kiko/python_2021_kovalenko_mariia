import turtle as t
import math

t.speed(10)
t.shape('turtle')

def polygon(n):
  R = 20*(n - 2)
  for i in range(n):
    t.fd(2 * R * math.sin(math.pi/n))
    t.left(360/n)

def polygons(n):
  for i in range(3, n + 3):
    t.penup()
    t.fd(20)
    t.pendown()

    t.left(90 + 180/i)
    polygon(i)
    t.right(90 + 180/i)

polygons(10)
