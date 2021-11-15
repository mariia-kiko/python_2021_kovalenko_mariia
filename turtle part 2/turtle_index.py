import turtle as t

t.speed(10)
t.shape('turtle')

# 1: digit consists this part 
digit_parts = [
  (1, 1, 1, 1, 1, 1, 0, 0, 0),
  (1, 1, 0, 0, 0, 0, 1, 0, 0),
  (1, 0, 1, 0, 0, 1, 0, 0, 1),
  (0, 0, 0, 0, 0, 1, 1, 1, 1),
  (1, 1, 0, 0, 1, 0, 0, 1, 0),
  (0, 1, 1, 0, 1, 1, 0, 1, 0),
  (0, 1, 1, 1, 0, 0, 1, 1, 0),
  (0, 0, 0, 1, 0, 1, 1, 0, 0),
  (1, 1, 1, 1, 1, 1, 0, 1, 0),
  (1, 0, 0, 0, 1, 1, 0, 1, 1)
]

def move(x_next, y_next, is_pendown):
  if is_pendown:
    t.pendown()
  else:
    t.penup()
  t.goto(x_next, y_next)


def digit_draw(digit, x, y):
  for i in range(9):
    move(x[i], y[i], digit_parts[int(digit)][i])


def draw_index(index):
  # coordinates of digit angles
  x = [30, 30, 0, 0, 0, 30, 0, 30, 0]
  y = [30, 0, 0, 30, 60, 60, 30, 30, 0]

  # start from the left part of the screen
  for k in range(9):
    x[k] -= 150

  # drawing digits one by one
  for i in range(0, len(index)):
    # start from right highest angle
    move(x[0], 60, 0)
    
    digit_draw(index[i], x, y)

    # next digit's X coordinate
    for j in range(9):
      x[j] += 50

draw_index('141700')
