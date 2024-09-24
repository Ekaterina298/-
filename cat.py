import pygame
from pygame.draw import *

def draw_cat(surface, x, y, width, height, color):
    '''
    Рисует зайца на экране.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    body_width = width // 2
    body_height = height // 2
    body_y = y + body_height // 2
    draw_body(surface, x, body_y, body_width, body_height, "green")

    head_size = height // 3.5
    draw_head(surface, x, y - head_size // 2.5, head_size, "green")

    ear_height = height // 5
    ear_y = y - height // 3 + ear_height // 2
    for ear_x in (x - head_size // 4, x + head_size // 4):
        draw_ear(surface, ear_x, ear_y, width // 8, ear_height, "green")

    leg_height = height // 10
    leg_y = y + height // 2 - leg_height // 2
    for leg_x in (x - width // 5, x + width // 5):
        draw_leg(surface, leg_x, leg_y, width // 6, leg_height, "blue")    
        
    
    
    tail_height = height//9
    tail_width = width//2
    tail_y = height//2
    draw_tail(surface, x, tail_y, tail_width, tail_height, "green")
    
    hand_height = height//3
    hand_y = y + height//3
    for hand_x in (x - width//15, x + width//15):
        draw_hand(surface, hand_x, hand_y, width//9, hand_height, "blue")
    
    nose_size = height//8
    draw_nose(surface, x, y - nose_size//2, nose_size, "blue")
    
    eye_size = height//4
    eye_y = y - height//8
    for eye_x in (x-eye_size//4, x+eye_size//4):
        draw_eyes(surface, eye_x, eye_y, eye_size, "blue")

def draw_tail(surface, x, y, width, height, color):
    s = pygame.Surface((width, height),pygame.SRCALPHA, 32)
    s = s.convert_alpha()
    ellipse(s, color, (0, 0, width, height))
    s = pygame.transform.rotate(s, 45)
    surface.blit(s, (x, y))
    

def draw_body(surface, x, y, width, height, color):
    '''
    Рисует тело зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))

def draw_hand(surface, x, y, width, height, color):
    ellipse(surface, color, (x - width//2, y - height//2, width, height) )
def draw_head(surface, x, y, size, color):
    '''
    Рисует голову зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    size - диаметр головы
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    circle(surface, color, (x, y), size // 2)

def draw_eyes(surface, x, y, size, color):
    circle(surface, color, (x,y), size//20)

def draw_nose(surface, x, y, size, color):
    circle(surface, color, (x,y), size//15)

def draw_ear(surface, x, y, width, height, color):
    '''
    Рисует ухо зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    polygon(surface, color, ((x - width // 2, y + height // 2), (x, y - height // 2), (x+width //2, y + height // 2)))
    # ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_leg(surface, x, y, width, height, color):
    '''
    Рисует ногу зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

draw_cat(screen, 200, 200, 400, 400, "red")

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
