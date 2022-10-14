class level:
    def __init__(self, x, y, rect_xpos, rect_ypos, loading):
        self.x = x
        self.y = y
        self.rect_xpos = rect_xpos
        self.rect_ypos = rect_ypos
        self.loading = loading

    def create_level(self):

        gras = pygame.image.load("graphics/tiles/Grass_64x64.png")
        brick = pygame.image.load("graphics/tiles/Dirt_Road_64x64.png")
        dirt = pygame.image.load("graphics/tiles/Brick_Wall_64x64.png")
        magma = pygame.image.load("graphics/tiles/Magma_Floor_64x64.png")

        rand = random.randint(0, 4)
        if self.x <= 30:
            if rand == 0 or rand == 1 or rand == 2:
                screen.blit(gras, (self.rect_xpos, self.rect_ypos))
            elif rand == 3:
                screen.blit(brick, (self.rect_xpos, self.rect_ypos))
            else:
                screen.blit(dirt, (self.rect_xpos, self.rect_ypos))
            self.rect_xpos += 64
            self.x += 1
        elif self.rect_ypos <= 1080 and self.rect_xpos >= 1920:
            self.rect_xpos = 0
            self.rect_ypos += 64
            self.x = 0
            self.y += 1

            print(str(self.x) + " <- X 30 | 17 Y -> " + str(self.y))






----------------------------------------------------------------------------------------------

import pygame
import sys
import random

w = 0
h = 0
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
gras_ar = " "
dirt = pygame.image.load("graphics/tiles/Dirt_Road_64x64.png")
dirt_ar = "D"
brick = pygame.image.load("graphics/tiles/Brick_Wall_64x64.png")
brick_ar = "B"
timer = pygame.time.Clock()


screen = pygame.display.set_mode([1920,1080])
runtime = True
gen = True
while runtime:

    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if pressed[pygame.K_ESCAPE]:
            runtime = False

    if w == 30 and h == 17:
        gen = False

    while gen:
        rand = random.randint(0, 4)
        if w <= 30:
            if rand == 0 or rand == 1 or rand == 2:
                screen.blit(gras, (rect_xpos, rect_ypos))
            elif rand == 3:
                screen.blit(brick, (rect_xpos, rect_ypos))
            else:
                screen.blit(dirt, (rect_xpos, rect_ypos))
            rect_xpos += 64
            w += 1
        elif rect_ypos <= 1080 and rect_xpos >= 1920:
            rect_xpos = 0
            w = 0
            rect_ypos += 64
        else:
            break

    #timer.tick(60)
    pygame.display.update()