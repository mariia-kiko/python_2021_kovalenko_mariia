import turtle as t

t.speed(10)
t.shape('turtle')
t.right(90)

def butterfly(n, R):
  for i in range(n):
    t.circle(R + (i-1)*10)
    t.circle(-R - (i-1)*10)
    
butterfly(10, 25)
