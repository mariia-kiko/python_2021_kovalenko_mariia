import turtle as t

t.speed(10)
t.shape('turtle')

def spider (n):
    for i in range(n):
        t.pendown()
        t.forward(100)
        t.stamp()
        t.left(180)
        t.forward(100)
        t.left(150)

spider(12)
