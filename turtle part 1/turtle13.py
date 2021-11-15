import turtle as t
import math

t.speed(10)
t.shape('turtle')

def arc(r):
  for i in range(30):
    t.fd(r * math.pi/60)
    t.left(6)

def move(x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()

def ccircle(r, color):
  t.fillcolor(color)
  t.begin_fill()
  t.circle(r)
  t.end_fill()

def smile():
  ccircle(100, "yellow")
  move(-40, 110)
  ccircle(15, "blue")
  move(40, 110)
  ccircle(15, "blue")
  move(0, 90)
  t.pencolor("black")
  t.pensize(10)
  t.right(90)
  t.forward(10)
  move(-40, 70)
  t.pencolor("red")
  arc(80)
  
