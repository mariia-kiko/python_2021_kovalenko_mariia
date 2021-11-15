import pygame
import math 
from pygame.draw import *

pygame.init()
FPS = 30

#LIST OF COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHTGRAY = (200, 200, 200)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (250, 150, 150)
RED = (255, 0, 0)
BROWN1 = (100, 60, 0)
BROWN2 = (150, 120, 20)
ORANGE = (210, 110, 0)
LIGHTBLUE = (160, 180 , 255)
LLBLUE = (210, 230, 255)
LIGHTGREEN = (160, 250, 100)
#SCREEN
x1 = 450
y1 = 600
k = 2.3
screen = pygame.display.set_mode((x1, y1))
screen.fill(BROWN1)
rect(screen, BROWN2,(0, y1/k, x1, y1 - (y1/k)))

def window (x, y, width, height): #x, y - координаты левого верхнего угла
     rect(screen, LLBLUE, (x, y, width, height))
     rect(screen, LIGHTBLUE, (x + 5, y + 5, (width/2) - 10, (height/3)))
     rect(screen, LIGHTBLUE, (x + width - 5 + 10 - (width/2), y + 5, (width/2) - 10, (height/3)))
     rect(screen, LIGHTBLUE, (x + 5, y + 10 + (height/3), (width/2) - 10, (2*height/3) - 15))
     rect(screen, LIGHTBLUE, (x + width - 5 + 10 - (width/2), y + 10 + (height/3), (width/2) - 10, (2*height/3) - 15))
window (270, 20, x1 - 5 - 270, (y1/k) - 25)

def cat (x, y, a, b, color, eyecolor, earcolor): #a, b - большая и малая полуоси эллипса-туловища кота; x, y - координаты левой вершины эллипса-туловища кота
    ellipse(screen, color, (x + a - (a/12.5), y - (b/5), a/2, b/2.5))
    ellipse(screen, BLACK, (x + a - (a/12.5), y - (b/5), a/2, b/2.5), 1)
    ellipse(screen, color, (x, y - (b/2),  a, b))
    ellipse(screen, BLACK, (x, y - (b/2),  a, b), 1)
    ellipse(screen, color, (x - (a/17), y - (b/18), a/8, b/1.95))
    ellipse(screen, BLACK, (x - (a/17), y - (b/18), a/8, b/1.95), 1)
    circle(screen, color, (x, y - (b/26)), b/2.5)
    circle(screen, BLACK, (x, y - (b/26)), b/2.5, 1)
    ellipse(screen, color, (x + (a/10), y + (b/4), a/4.2, b/3.8))
    ellipse(screen, BLACK, (x + (a/10), y + (b/4), a/4.2, b/3.8), 1)
    circle(screen, color, (x + a - (a/6.7), y + (a/6.7)), a/6.7)
    circle(screen, BLACK, (x + a - (a/6.7), y + (a/6.7)), a/6.7, 1)
    ellipse(screen, color, (x + a - (a/16), y + (a/6), a/8, b/1.95))
    ellipse(screen, BLACK, (x + a - (a/16), y + (a/6), a/8, b/1.95), 1)
    ellipse(screen, eyecolor, (x - b/3.8, y - (b/26) - b/7.5, b/5.1, 1.7*b/7.5))
    ellipse(screen, BLACK, (x - b/3.8, y - (b/26) - b/7.5, b/5.1, 1.7*b/7.5), 1)
    ellipse(screen, eyecolor, (x + b/3.8 - b/5, y - (b/26) - b/7.5, b/5.1, 1.7*b/7.5))
    ellipse(screen, BLACK, (x + b/3.8 - b/5, y - (b/26) - b/7.5, b/5.1, 1.7*b/7.5),1)
    ellipse(screen, BLACK, (x - b/3.8 + b/10, y - (b/26) - b/7.7, b/25, 1.5*b/7.5))
    ellipse(screen, BLACK, (x + b/3.8 - b/5 + b/10, y - (b/26) - b/7.7, b/25, 1.5*b/7.5))
    ellipse(screen, WHITE, (x - b/3.8 + b/15, y - (b/26) - b/7.5 + (b/20), b/12, 1.7*b/(7.5*7)))
    ellipse(screen, WHITE, (x + b/3.8 - b/5 + b/15, y - (b/26) - b/7.5 + (b/20), b/12, 1.7*b/(7.5*7)))
    polygon(screen, PINK, [(x - 0.9*b/2.5, y - (b/26) - 0.8*b/2.5), (x - 0.9*b/2.5, y - (b/26) - 0.25*b/2.5), (x - 0.55*b/2.5, y - (b/26) - 0.7*b/2.5)])
    polygon(screen, BLACK, [(x - 0.9*b/2.5, y - (b/26) - 0.8*b/2.5), (x - 0.9*b/2.5, y - (b/26) - 0.25*b/2.5), (x - 0.55*b/2.5, y - (b/26) - 0.7*b/2.5)], 1)
    polygon(screen, earcolor, [(x - 0.9*b/2.5 - 1, y - (b/26) - 0.8*b/2.5 + 1), (x - 0.9*b/2.5, y - (b/26) - 0.25*b/2.5 - 1), (x - 0.55*b/2.5 + 1, y - (b/26) - 0.7*b/2.5)], 5)
    aalines(screen, earcolor, True, [(x - 0.9*b/2.5 - 1, y - (b/26) - 0.8*b/2.5 + 1), (x - 0.9*b/2.5, y - (b/26) - 0.25*b/2.5 - 1), (x - 0.55*b/2.5 + 1, y - (b/26) - 0.7*b/2.5)], 2)
    #polygon(screen, BLACK, [(x - 0.9*b/2.5 - 1, y - (b/26) - 0.8*b/2.5 + 1), (x - 0.9*b/2.5, y - (b/26) - 0.25*b/2.5 - 1), (x - 0.55*b/2.5 + 1, y - (b/26) - 0.7*b/2.5)], 1)
    polygon(screen, PINK, [(x + 0.9*b/2.5, y - (b/26) - 0.8*b/2.5), (x + 0.9*b/2.5, y - (b/26) - 0.25*b/2.5), (x + 0.55*b/2.5, y - (b/26) - 0.7*b/2.5)])
    #polygon(screen, BLACK, [(x + 0.9*b/2.5, y - (b/26) - 0.8*b/2.5), (x + 0.9*b/2.5, y - (b/26) - 0.25*b/2.5), (x + 0.55*b/2.5, y - (b/26) - 0.7*b/2.5)], 1)
    polygon(screen, earcolor, [(x + 0.9*b/2.5 - 1, y - (b/26) - 0.8*b/2.5 + 1), (x + 0.9*b/2.5, y - (b/26) - 0.25*b/2.5 - 1), (x + 0.55*b/2.5 + 1, y - (b/26) - 0.7*b/2.5)], 5)
    aalines(screen, earcolor, True,[(x + 0.9*b/2.5 - 1, y - (b/26) - 0.8*b/2.5 + 1), (x + 0.9*b/2.5, y - (b/26) - 0.25*b/2.5 - 1), (x + 0.55*b/2.5 + 1, y - (b/26) - 0.7*b/2.5)], 2)
    #polygon(screen, BLACK, [(x + 0.9*b/2.5 - 1, y - (b/26) - 0.8*b/2.5 + 1), (x + 0.9*b/2.5, y - (b/26) - 0.25*b/2.5 - 1), (x + 0.55*b/2.5 + 1, y - (b/26) - 0.7*b/2.5)],1)
    polygon(screen, PINK, [(x, y - b/26 + 0.4*b/2.5), (x - b/25, y - b/26 + 0.3*b/2.5), (x + b/25, y - b/26 + 0.3*b/2.5)])
    #polygon(screen, BLACK, [(x, y - b/26 + 0.4*b/2.5), (x - b/25, y - b/26 + 0.3*b/2.5), (x + b/25, y - b/26 + 0.3*b/2.5)], 1)
    aalines(screen, BLACK, True, [[x, y - b/26 + 0.4*b/2.5], [x, y - b/26 + 0.55*b/2.5]], 1)
    arc(screen, BLACK, (x, y - b/26 + 0.45*b/2.5, 0.2*b/2.5, 0.2*b/2.5), math.pi, 2*math.pi, 1)
    arc(screen, BLACK, (x - 0.2*b/2.5, y - b/26 + 0.45*b/2.5, 0.2*b/2.5, 0.2*b/2.5), math.pi, 2*math.pi, 1)
    arc(screen, BLACK, (x + 0.25*b/2.5, y - b/26 + 0.4*b/2.5, 0.9*b/2.5, 0.2*b/2.5), math.pi/10, math.pi, 1)
    arc(screen, BLACK, (x + 0.25*b/2.5, y - b/26 + 0.5*b/2.5, 0.9*b/2.5, 0.2*b/2.5), math.pi/10, 6*math.pi/7, 1)
    arc(screen, BLACK, (x + 0.25*b/2.5, y - b/26 + 0.3*b/2.5, 0.9*b/2.5, 0.2*b/2.5), math.pi/10, math.pi, 1)
    arc(screen, BLACK, (x - 0.25*b/2.5 - 0.9*b/2.5, y - b/26 + 0.4*b/2.5, 0.9*b/2.5, 0.2*b/2.5), math.pi/10, math.pi, 1)
    arc(screen, BLACK, (x - 0.25*b/2.5 - 0.9*b/2.5, y - b/26 + 0.5*b/2.5, 0.9*b/2.5, 0.2*b/2.5), math.pi/10, 6*math.pi/7, 1)
    arc(screen, BLACK, (x - 0.25*b/2.5 - 0.9*b/2.5, y - b/26 + 0.3*b/2.5, 0.9*b/2.5, 0.2*b/2.5), math.pi/10, math.pi, 1)
cat((250/4), (y1/k) + (130/2) + 20, 250, 130, ORANGE, LIGHTGREEN, BROWN1)

def ball(x, y, r):
    arc(screen, BLACK, (x, y, 2*r, r/4), 0, math.pi)
    arc(screen, BLACK, (x + 2*r, y, r, r/4), math.pi, 2*math.pi)
    arc(screen, BLACK, (x + 2*r + r, y, 1.5*r, r/4), 0, math.pi)
    circle(screen, GRAY, (x, y), r)
    circle(screen, BLACK, (x, y), r, 1)
    arc (screen, BLACK, (x - r/2, y - r/2, r, r/4,), 0, math.pi)
    arc (screen, BLACK, (x - r/2, y - r/4, r, r/4,), 0, math.pi)
    arc (screen, BLACK, (x - r/2, y , r, r/4,), 0, math.pi)
    arc (screen, BLACK, (x - r/2, y - r/2, r/4, r,), 0.5*math.pi, 1.5*math.pi)
    arc (screen, BLACK, (x , y - r/2, r/4, r,), 0.5*math.pi, 1.5*math.pi)
    arc (screen, BLACK, (x - r/4, y - r/2, r/4, r,), 0.5*math.pi, 1.5*math.pi)
ball(250, y1 - 100, 30)    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
