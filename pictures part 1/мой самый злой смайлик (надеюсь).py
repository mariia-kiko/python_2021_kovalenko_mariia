import pygame
from pygame.draw import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHTGRAY = (200, 200, 200)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)
FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill(LIGHTGRAY)
circle(screen, YELLOW, (200, 200), 100)
circle(screen, BLACK, (200, 200), 100, 3)

def eye (x, y, r1, r2):
    circle(screen, RED, (x, y), r1)
    circle(screen, BLACK, (x, y), r1, 3)
    circle(screen, BLACK, (x, y), r2)
    
eye(160, 175, 20, 6)
eye(240, 175, 15, 5)
rect(screen, BLACK, (160, 230, 80, 17))
polygon(screen, BLACK, [(110, 125), (107, 130), (190, 167), (187, 172)])
aalines(screen, BLACK, True, [(110, 125), (107, 130), (190, 167), (187, 172)])
polygon(screen, BLACK, [(290, 125), (293, 130), (215, 167), (218, 172)])
aalines(screen, BLACK, True,[(290, 125), (293, 130), (215, 167), (218, 172)] )

pygame.display.update()
clock = pygame.time.Clock()
finished = False
       
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
