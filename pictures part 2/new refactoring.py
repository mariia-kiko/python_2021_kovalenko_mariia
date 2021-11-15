import pygame
from pygame.draw import *
import math as m
pygame.init()

#SCREEN PARAMETERS
WIDTH = 1000
HEIGHT = 600

#LIST OF COLORS
LIGHT_OLIVE = (206, 235, 206)
BLUE = (44, 117, 255)
YELLOW = (237, 255, 33)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (168,47,20)
LIGHT_RED = (235, 76, 66)

FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))

#FUNCTIONS
def background (x, y, color1 = LIGHT_OLIVE, color2 = BLUE, color3 = YELLOW):
    '''
        x, y - coordinates of upper left corner of the background surface
        color1, color2, color3 - background colors in RGB (LIGHT_OLIVE, BLUE, YELLOW - default colors)
    '''
    surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    surf.set_alpha(255)
    rect(screen, color1, (0, 0 ,WIDTH, HEIGHT/3))
    rect(screen, color2, (0, HEIGHT/3, WIDTH, HEIGHT/3))
    rect(screen, color3, (0, 2*HEIGHT/3, WIDTH, HEIGHT/3))
    screen.blit(surf, (x, y))    

def cloud (x0, y0, r, cloud_color = WHITE):
    '''
        x0, y0 - coordinates of upper left corner of the cloud surface
        r - radius of each circle
        cloud_color - color of cloud in RGB (WHITE - default color)      
    '''
    surf = pygame.Surface((6*r, 4*r), pygame.SRCALPHA)
    surf.set_alpha(255)
    for i in range (3):
        circle(surf, cloud_color, ((i+2)*r, 1.5*r), r)
        circle(surf, BLACK, ((i+2)*r, 1.5*r), r, 1)
    for j in range (4):
        circle(surf, cloud_color, (2*r - 2*r/3 + j*r, 2.5*r), r)
        circle(surf, BLACK, (2*r - 2*r/3 + j*r, 2.5*r), r, 1)
    screen.blit(surf, (x0, y0))
    
def sun (x0, y0, r, color = YELLOW):
    '''
        x0, y0 - coordinates of center of the Sun
        r - radius of the Sun
        color - Sun color in RGB (YELLOW - default color)
    '''
    circle(screen, color, (x0, y0), r)

def umbrella(x0, y0, hat_width, hat_height, stick_width, stick_height, n, hat_color = LIGHT_RED, stick_color = BROWN):
    '''
       x0, y0 - coordinates of upper left corner of the umbrella surface
       hat_width, hat_height - length parameters of umbrella hat in pixels
       stick_width, stick_height - length parameters of umbrella stick in pixels
       n - number of lines on umbrella hat
       hat_color, stick_color - colors of umbrella hat and stick in RGB (LIGHT_RED, BROWN - default colors)
    '''
    surf = pygame.Surface((hat_width, hat_height + stick_height), pygame.SRCALPHA)
    surf.set_alpha(255)
    rect(surf, stick_color, (0.5*hat_width - 0.5*stick_width, hat_height, stick_width, stick_height))
    polygon(surf, hat_color, [(0, hat_height), (0.5*hat_width, 0), (hat_width, hat_height)])
    for i in range (n + 1):
        line(surf, BLACK, (i*hat_width/(n+1), hat_height), (0.5*hat_width, 0))
    screen.blit(surf, (x0, y0))

def boat (x0, y0, bottom_width, boat_height, stick_width, stick_height, boat_color = BROWN, sail_color = WHITE):
    '''
        x0, y0 - coordinates of upper left corner of the boat surface
        bottom_width, boat_heigth - length parameters of boat in pixels
        stick_width, stick_height - length parameters of stick in pixels
        boat_color, sail_color - colors in RGB (BROWN, WHITE - default colors)
    '''
    surf = pygame.Surface((1.5*bottom_width + boat_height, boat_height + stick_height), pygame.SRCALPHA)
    surf.set_alpha(255)
    rect(surf, boat_color, (boat_height, stick_height, bottom_width, boat_height))
    polygon(surf, boat_color, [(bottom_width + boat_height, stick_height),
                               (1.5*bottom_width + boat_height, stick_height),
                               (bottom_width + boat_height, stick_height + boat_height)])
    arc(surf, boat_color, [0, stick_height - boat_height, 2*boat_height, 2*boat_height],m.pi,m.pi*1.5, boat_height)
    arc(surf, boat_color, [1, stick_height - boat_height, 2*boat_height, 2*boat_height],m.pi,m.pi*1.5, boat_height)
    arc(surf, boat_color, [2, stick_height - boat_height, 2*boat_height, 2*boat_height],m.pi,m.pi*1.5, boat_height)
    rect(surf, BLACK, (0.5*bottom_width + boat_height, 0, stick_width, stick_height))
    polygon(surf, sail_color, [(0.5*bottom_width + boat_height + stick_width, 0),
                               (bottom_width + boat_height + stick_width, 0.4*stick_height),
                               (0.7*bottom_width + boat_height + stick_width, 0.4*stick_height)])
    polygon(surf, sail_color, [(0.5*bottom_width + boat_height + stick_width, 0.8*stick_height),
                               (bottom_width + boat_height + stick_width, 0.4*stick_height),
                               (0.7*bottom_width + boat_height + stick_width, 0.4*stick_height)])
    line(surf, BLACK, (0.5*bottom_width + boat_height + stick_width, 0),
                               (bottom_width + boat_height + stick_width, 0.4*stick_height))      
    line(surf, BLACK, (0.5*bottom_width + boat_height + stick_width, 0.8*stick_height),
                               (bottom_width + boat_height + stick_width, 0.4*stick_height))
    line(surf, BLACK, (bottom_width + boat_height + stick_width, 0.4*stick_height),
                               (0.7*bottom_width + boat_height + stick_width, 0.4*stick_height))
    line(surf, BLACK, (0.7*bottom_width + boat_height + stick_width, 0.4*stick_height),
                               (0.5*bottom_width + boat_height + stick_width, 0.8*stick_height))
    line(surf, BLACK, (0.7*bottom_width + boat_height + stick_width, 0.4*stick_height),
                               (0.5*bottom_width + boat_height + stick_width, 0))
    circle(surf, WHITE, (0.9*bottom_width + boat_height, stick_height + 0.5*boat_height), 0.35*boat_height)   
    circle(surf, BLACK, (0.9*bottom_width + boat_height, stick_height + 0.5*boat_height), 0.35*boat_height, 2)
    screen.blit(surf, (x0, y0))

#USING FUNCTIONS
background(0, 0)
cloud(10, 10, 30, WHITE)
sun(830, 100, 50)    
umbrella(525, 350, 140, 30, 20, 180, 6)
boat(300, 70, 250, 50, 10, 200)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
