import turtle as t
t.shape('turtle')
for i in range(10):
        t.forward(10*i + 10)
        t.left(90)
        t.forward(10*i + 10)
        t.left(90)
        t.forward(10*i + 10)
        t.left(90)
        t.forward(10*i + 10)
        t.goto(-5*(i+1), -5*(i+1))
        t.pendown()
        turtle.left(90)
