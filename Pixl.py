import pygame
import sys
from data.font import *
from pygame.locals import *

clock = pygame.time.Clock()
pygame.init()
icon = pygame.image.load('data/icon.png')
icon.set_colorkey((0, 0, 0))
pygame.display.set_caption('Pixl')
pygame.display.set_icon(icon)

WINDOW_SIZE = (895, 600)
screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
canvas = pygame.Surface((447.5, 300))
palette = pygame.Surface((95, 600))
mouse = pygame.image.load('data/mouse.png')

clicking = False
drawing = False
bucket = False
drag = False
drag1 = False
drag2 = False
drag3 = False
menu = False
hlp = False

font = Font('data/font.png')

menurect = pygame.Rect(0, 0, 43, 20)
backrect = pygame.Rect(0, 222, 33, 20)
helprect = pygame.Rect(0, 20, 33, 20)

slider = pygame.Rect(85, 22, 5, 13)
slider2 = pygame.Rect(85, 72, 5, 13)
slider3 = pygame.Rect(85, 122, 5, 13)
slider4 = pygame.Rect(42, 172, 5, 13)

status = 0

particles = []

while True:
    px, py = pygame.mouse.get_pos()
    w, h = pygame.display.get_surface().get_size()
    palette = pygame.Surface((95, h))

    if not menu:
        palette.fill((50, 50, 50))
        pygame.draw.rect(palette, (50, 50, 50), menurect)
        font.render(palette, 'Colors', (0, 5))
        pygame.draw.rect(palette, (50, 50, 50), helprect)
        font.render(palette, 'Help', (0, 25))

    if menu:
        palette.fill((32, 49, 107))
        font.render(palette, 'Red', (0, 5))
        pygame.draw.rect(palette, (255, 255, 255), (0, 25, 90, 5))
        if slider.x > 85:
            slider.x = 85
            pygame.draw.rect(palette, (0, 192, 207), slider)
        else:
            pygame.draw.rect(palette, (0, 192, 207), slider)
        font.render(palette, 'Green', (0, 55))
        pygame.draw.rect(palette, (255, 255, 255), (0, 75, 90, 5))
        if slider2.x > 85:
            slider2.x = 85
            pygame.draw.rect(palette, (0, 192, 207), slider2)
        else:
            pygame.draw.rect(palette, (0, 192, 207), slider2)
        font.render(palette, 'Blue', (0, 105))
        pygame.draw.rect(palette, (255, 255, 255), (0, 125, 90, 5))
        if slider3.x > 85:
            slider3.x = 85
            pygame.draw.rect(palette, (0, 192, 207), slider3)
        else:
            pygame.draw.rect(palette, (0, 192, 207), slider3)
        font.render(palette, 'Size', (0, 155))
        pygame.draw.rect(palette, (255, 255, 255), (0, 175, 90, 5))
        if slider4.x > 85:
            slider4.x = 85
            pygame.draw.rect(palette, (0, 192, 207), slider4)
        else:
            pygame.draw.rect(palette, (0, 192, 207), slider4)
        pygame.draw.rect(palette, (32, 49, 107), backrect)
        font.render(palette, 'Back', (0, 222))
        rec = pygame.Rect(0, 242, slider4.x / 5, slider4.x / 5)
        pygame.draw.rect(palette, (slider.x * 3, slider2.x * 3, slider3.x * 3), rec)
    size = slider4.x / 5

    if hlp:
        palette.fill((48, 147, 46))
        font.render(palette, 'X - Erase all', (0, 0))
        font.render(palette, 'N - Pencil', (0, 20))
        font.render(palette, 'B - Bucket', (0, 40))
        font.render(palette, 'E - Eraser', (0, 60))
        font.render(palette, 'Preview in', (0, 80))
        font.render(palette, "'Colors' menu", (0, 100))
        font.render(palette, "under 'Back'", (0, 120))
        font.render(palette, 'button', (0, 140))
        pygame.draw.rect(palette, (48, 147, 46), backrect)
        font.render(palette, 'Back', (0, 222))

    pencilrect = pygame.Rect(px / 2, py / 2, size, size)
    eraserrect = pygame.Rect(px / 2, py / 2, 15, 15)

    red = slider.x * 3
    green = slider2.x * 3
    blue = slider3.x * 3
    colour = (red, green, blue)

    if drawing:
        if status == 0:
            pygame.draw.rect(canvas, (slider.x * 3, slider2.x * 3, slider3.x * 3), pencilrect)
        if status == 1:
            pygame.draw.rect(canvas, (0, 0, 0), eraserrect)
        if status == 2:
            canvas.fill((slider.x * 3, slider2.x * 3, slider3.x * 3))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_x:
                canvas.fill((0, 0, 0))
            if event.key == K_b:
                status = 2
            if event.key == K_e:
                status = 1
            if event.key == K_n:
                status = 0
                bucket = False
            if event.key == K_m:
                menu = True
            if event.key == K_r:
                menu = False
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if slider.collidepoint(px / 2, py / 2):
                    drag = True
                    drawing = False
                if slider2.collidepoint(px / 2, py / 2):
                    drag1 = True
                    drawing = False
                if slider3.collidepoint(px / 2, py / 2):
                    drag2 = True
                    drawing = False
                if slider4.collidepoint(px / 2, py / 2):
                    drag3 = True
                    drawing = False
                if menurect.collidepoint(px / 2, py / 2):
                    menu = True
                if backrect.collidepoint(px / 2, py / 2):
                    menu = False
                    hlp = False
                    sizew = False
                clicking = True
                if not menu:
                    if helprect.collidepoint(px / 2, py / 2):
                        hlp = True
                if bucket is True:
                    canvas.fill(colour)
                drawing = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                drag = False
                drag1 = False
                drag2 = False
                drag3 = False
                drawing = False
                clicking = False
        if event.type == MOUSEMOTION:
            if drag:
                slider.x = px / 2
            if drag1:
                slider2.x = px / 2
            if drag2:
                slider3.x = px / 2
            if drag3:
                slider4.x = px / 2

    canvas.blit(palette, (0, 0))
    surface = pygame.transform.scale(canvas, WINDOW_SIZE)
    screen.blit(surface, (0, 0))
    pygame.display.update()
    clock.tick(1000)
