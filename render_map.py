import pygame
import sys
import random

width = 0
height = 0
rect_xpos = 0
rect_ypos = 0
materials = [" ", " ", " ", "D","B"]          # gras, dirt, brick
gen_map = [[],
           [],
           [],
           [],
           [],
           [],
           [],
           [],
           [],
           [],
           [],
           [],
           [],
           [],
           [],
           [],
           []
           ]
rand = random.randint(0,2)
gras = pygame.image.load("graphics/tiles/Grass_64x64.png")
dirt = pygame.image.load("graphics/tiles/Dirt_Road_64x64.png")
brick = pygame.image.load("graphics/tiles/Brick_Wall_64x64.png")
timer = pygame.time.Clock()


screen = pygame.display.set_mode([1920,1080])
runtime = True
gen = True
while runtime:

    if width == 30 and height == 17:
        gen = False

    while gen:
        rand = random.randint(0, 4)
        if width <= 30:
            if rand == 0 or rand == 1 or rand == 2:
                screen.blit(gras, (rect_xpos, rect_ypos))
                gen_map [[width]] = materials[rand]
            elif rand == 3:
                screen.blit(brick, (rect_xpos, rect_ypos))
            else:
                screen.blit(dirt, (rect_xpos, rect_ypos))
            rect_xpos += 64
            width += 1
        elif rect_ypos <= 1080 and rect_xpos >= 1920:
            rect_xpos = 0
            width = 0
            rect_ypos += 64
        else:
            break


    #timer.tick(60)
    pygame.display.update()