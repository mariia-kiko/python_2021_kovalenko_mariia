import pygame
from pygame.draw import *
from random import randint, choice, random
import math
import csv

pygame.init()
pygame.font.init()
Name = input("Введите ваше имя: ") 
FPS = 60
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE]


class Target:
    '''
    Создание родительского класса мишеней
    '''
    def __init__(self):
        self.new_target()

    def new_target(self):
        '''
        Задает параметры мишени - координаты, размеры, скорость, направление скорости
        '''
        self.color = choice(COLORS)
        self.r = randint(10, 30)
        self.x = randint(self.r, WIDTH-self.r)
        self.y = randint(self.r, HEIGHT-self.r)
        self.v = randint(100, 300)
        self.angle = random() * 2 * math.pi
        self.v_x = self.v * math.cos(self.angle)
        self.v_y = self.v * math.sin(self.angle)


class Circle(Target):
    '''
    Создание дочернего класса мишеней - кружочка
    '''
    def clicked(self, event):
        '''
        Начисление 1 очка за попадание в кружочек.
        '''
        # Проверка условия попадания в круг.
        if math.dist(event.pos, (self.x, self.y)) <= self.r:
            score.increase(1)
            self.new_target()

    def move(self):
        '''
        Прорисовка и движение кружочка. Проверка условия невылета кружочка за пределы окна.
        '''
        # Отражение под случайным углом при достижении правой стенки.
        if self.x > WIDTH-self.r:
            self.angle = (random() + 1) * math.pi
        # Отражение под случайным углом при достижении левой стенки.
        elif self.x < self.r:
            self.angle = random() * math.pi
        # Отражение под случайным углом при достижении нижней стенки.
        if self.y > HEIGHT-self.r:
            self.angle = (random() + 1.5) * math.pi
        # Отражение под случайным углом при достижении верхней стенки.
        elif self.y < self.r:
            self.angle = (random() + 0.5) * math.pi
        # Параметры скорости и координат кружочка в каждом кадре.  
        self.v_x = self.v * math.sin(self.angle)
        self.v_y = self.v * math.cos(self.angle) * (-1)
        self.x += self.v_x / FPS
        self.y += self.v_y / FPS
        # Прорисовка  кружочка.
        circle(screen, self.color, (int(self.x), int(self.y)), self.r)


class Square(Target):
    '''
    Создание дочернего класса мишеней - квадрата
    '''
    def clicked(self, event):
        '''
        Начисление 5 очков за попадание в квадрат
        '''
        # Проверка условия попадания в квадрат.
        if abs(event.pos[0] - self.x) <= self.r and abs(event.pos[1] - self.y) <= self.r:
            score.increase(5)
            self.new_target()

    def move(self):
        '''
        Прорисовка и движение квадрата. Проверка условия невылета квадрата за пределы поля.
        '''
        # Отражение под случайным углом при достижении правой стенки.
        if self.x > WIDTH-self.r:
            self.angle = (random() + 0.5) * math.pi
        # Отражение под случайным углом при достижении левой стенки.
        elif self.x < self.r:
            self.angle = (random() - 0.5) * math.pi
        # Отражение под случайным углом при достижении нижней стенки.
        if self.y > HEIGHT-self.r:
            self.angle = (random() + 1) * math.pi
        # Отражение под случайным углом при достижении верхней стенки.    
        elif self.y < self.r:
            self.angle = random() * math.pi
        # Изменение угла, под которым движется квадрат, при наведения курсора по нему. 
        if abs(pygame.mouse.get_pos()[0] - self.x) <= self.r and abs(pygame.mouse.get_pos()[1] - self.y) <= self.r:
            self.angle = math.atan2(self.y - pygame.mouse.get_pos()[1], self.x - pygame.mouse.get_pos()[0])
        # Параметры скорости и координат квадрата в каждом кадре.
        self.v_x = self.v * math.cos(self.angle)
        self.v_y = self.v * math.sin(self.angle)
        self.x += self.v_x / FPS
        self.y += self.v_y / FPS
        # Прорисовка  квадрата.
        rect(screen, self.color, [int(self.x - self.r), int(self.y - self.r), int(2*self.r), int(2*self.r)])

class Counter:
    '''
    Подсчет количества очков
    '''
    def __init__(self):
        self.count = 0

    def increase(self, prize):
        self.count += prize

    def draw(self):
        # Вывод количества очков на дисплей.
        surface_counter = labelFont.render(str(self.count), False, YELLOW)
        screen.blit(surface_counter, (0, 0))

       
# Создаем первую партию из 10 двигающихся кружочков из класса Circle.
circles = [Circle() for i in range(10)]
# Создаём 2 двигающихся квадрата из класса Square.
squares = [Square() for j in range(2)]
# Выводим количество очков.
score = Counter()
labelFont = pygame.font.SysFont('TimesNewRoman', 60)
pygame.display.update()
clock = pygame.time.Clock()
finished = False


# Основной цикл программы
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        # Проверяем выход из программы.
        if event.type == pygame.QUIT:
            finished = True
        # Проверяем попадание по мишени.   
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for circ in circles:
                circ.clicked(event)
            for square in squares:
                square.clicked(event)
    # Дальнейшее движение новых мишеней.
    for circ in circles:
        circ.move()
    for square in squares:
        square.move()
    score.draw()
    pygame.display.update()
    screen.fill(BLACK)



data = [{Name: score.count}]
with open('records.csv', 'a') as f:
    writer = csv.DictWriter(
        f, fieldnames = list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for d in data:
        writer.writerow(d)
pygame.quit()
