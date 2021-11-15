import turtle as t

t.speed(10)
t.shape('turtle')

def move(x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()

def star(n):
  t.left(90 + 90/n)
  for i in range(n):
    t.fd(100)
    t.left(180 - 180/n)

move(-100, -20)
star(5)
move(100, 50)
star(11)
