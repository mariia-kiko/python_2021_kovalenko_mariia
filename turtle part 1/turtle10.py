import turtle as t

t.speed(10)
t.shape('turtle')

def flower(n):
  for i in range(n):
    t.circle(50)
    t.circle(-50)
    t.left(180/n)

flower(3)
