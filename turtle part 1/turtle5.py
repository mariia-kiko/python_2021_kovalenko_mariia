import turtle as t
import math

t.speed(10)
t.shape('turtle')

def square(length, width):
  for i in range(4):
    t.fd(length)
    t.left(90)

def move_to_next(width):
  t.penup()
  t.right(135)
  t.fd(width)
  t.left(135)
  t.pendown()

def draw(length, width, n):
  for i in range(n):
    square(length + width/math.sqrt(2)*2*i, width)
    move_to_next(width)
    
    
draw(70, 20, 10)
