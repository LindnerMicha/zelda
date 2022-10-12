import pygame
import sys

pygame.display.set_caption("Zelda")
pygame.init()
screen = pygame.display.set_mode([1920, 1080])
clock = pygame.time.Clock()
fps = 60
maus_pos = pygame.mouse.get_pos()
maus_klick = pygame.mouse.get_pressed()                                         #((linke taste, mausrad, rechte taste))
pixel_font = pygame.font.Font("fonts/PixeloidSans.ttf", 30)
level_val = 0
k_up = pygame.K_w
k_down = pygame.K_s
k_left = pygame.K_a
k_right = pygame.K_d


playerImg = pygame.image.load("graphics/zelda_test_char.png").convert_alpha()
playerX = 370
playerY = 480
playerSpeed = 5

background = pygame.image.load("graphics/test_bgImg.jpg")

def textObjekt(text, pixel_font):
    textFlaeche = pixel_font.render(text, True, (0,0,0))
    return textFlaeche, textFlaeche.get_rect()

maus_aktiv = False
option = "Home"

def button( but_txt, but_x, but_y, but_laenge, but_hoehe, but_color_0, but_color_1):
    global maus_aktiv
    global option
    if maus_pos[0] > but_x and maus_pos[0] < but_x + but_laenge and maus_pos[1] > but_y and maus_pos[1] < but_y+but_hoehe:
        pygame.draw.rect(screen, but_color_1, (but_x, but_y, but_laenge, but_hoehe))
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if but_txt == "Start":
                option = "Start"
            elif but_txt == "Einstellungen":
                option = "Einstellungen"
            elif but_txt == "Credits":
                option = "Credits"
            elif but_txt == "Exit":
                sys.exit()
        if maus_klick[0] == 0:
            maus_aktiv = False
    else:
        pygame.draw.rect(screen, but_color_0, (but_x, but_y, but_laenge, but_hoehe))
    textGrund, textkasten = textObjekt(but_txt, pixel_font)
    textkasten.center = ((but_x+(but_laenge/2)),(but_y+(but_hoehe/2)))
    screen.blit(textGrund, textkasten)

def startscreen():
    screen.blit(background, (0, 0))
    button("Start",         50, 180, 500, 100, "White", "Green")
    button("Einstellungen", 50, 380, 500, 100, "White", "Green")
    button("Credits",       50, 580, 500, 100, "White", "Green")
    button("Exit",          50, 780, 500, 100, "White", "Green")

def zeichnen():
    pygame.display.update()


def level(level_val):
    if level_val == 0:
        background = pygame.image.load("graphics/lvl_text_bg.png")
        screen.blit(background, (0, 0))

def player(playerImg, playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))

runtime = True
while runtime:

    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if pressed[pygame.K_ESCAPE] and option == "Home":
            runtime = False
        if pressed[pygame.K_ESCAPE] and option != "Home":
            option = "Home"
    if pressed[k_up]:
        playerY -= 1*playerSpeed
    if pressed[k_down]:
        playerY += 1*playerSpeed
    if pressed[k_left]:
        playerX -= 1*playerSpeed
    if pressed[k_right]:
        playerX += 1*playerSpeed

    if option == "Home":
        startscreen()
    elif option == "Start":
        level(level_val)
        player(playerImg, playerX, playerY)
        pass
    elif option == "Credits":
        pass



    zeichnen()
    maus_pos = pygame.mouse.get_pos()
    maus_klick = pygame.mouse.get_pressed()
    clock.tick(fps)
    #pygame.time.wait(10)                        # 10 ms delay (wegen maus)



