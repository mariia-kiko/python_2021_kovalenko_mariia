from random import randint
import turtle as t
import math

t.speed(0)
amount_of_turtles = 20
steps_of_time = 10000
dt = 0.03

t.penup()
t.goto(-300, 300)
t.pendown()
t.pensize(3)
for i in range(4):
  t.fd(600)
  t.right(90)
t.hideturtle()


pool = [t.Turtle() for i in range(amount_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.shape('circle')
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.Vx = randint(-500, 500)
    unit.Vy = randint(-500, 500)



for i in range(steps_of_time):
    for unit in pool:
        unit.x = unit.xcor()
        unit.y = unit.ycor()
        unit.x += unit.Vx * dt
        unit.y += unit.Vy * dt
  
        unit.goto(unit.x, unit.y)

        if abs(unit.x) > 280:
          unit.x = 280 * unit.x / abs(unit.x)
          unit.Vx = -unit.Vx
        if abs(unit.y) > 280:
          unit.y = 280 * unit.y / abs(unit.y)
          unit.Vy = -unit.Vy
        
