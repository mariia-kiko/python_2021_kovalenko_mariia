import turtle as t
import math

t.shape('circle')
t.speed(0)
t.penup()
t.goto(-200, 0)
t.pendown()
dt = 0.05


def falling(v, theta, g, kappa):    #kappa - сопротивление воздуха, theta - угол между начальным вектором скорости и горизонтом
  x = -200.0
  y = 0.0
  vx = v * math.cos(theta * math.pi / 180)
  vy = v * math.sin(theta * math.pi / 180)
  for i in range(1000):
    ax = -kappa*(vx**2)
    ay = -g - (vy**2)*kappa
    x += vx*dt + ax*(dt**2)/2
    y += vy*dt + ay*(dt**2)/2
    vy += ay*dt
    vx += ax*dt
    t.goto(x, y)
    if y < 0:
      vy = -vy * 0.7
      y = 0


def floor():
  t.pensize(4)
  t.goto(-200, 0)
  t.goto(300, 0)
  t.goto(-200, 0)
  t.pensize(1)
  
  falling(100, 70, 9.81, 0.007)

floor()
