import turtle as t
import math
t.shape('circle')
x = -100
y = 0
dt = 0.5
#dt = 0
#x0 = 0
def parabola(v, theta, a, k):
    vx = v*math.cos(theta*math.pi/180)
    vy = v*math.sin(theta*math.pi/180)
    print(vx, vy)
    for i in range (500):
        x += vx*dt
        y += vy*dt - a*(dt**2)/2
        t.goto(x,y)
        if y < 0:
            v = 0.5*v
            y = 0
        
parabola(30, 60, 5, 6)


