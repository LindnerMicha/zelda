import pygame
import sys

pygame.display.set_caption("Zelda")
pygame.init()
screen = pygame.display.set_mode([1920, 1080]) #1920x1080
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
last_dir = [0, 0, 0, 0]

stehen = pygame.image.load("graphics/player/player_standing.png").convert_alpha()
rechtsgehen = [pygame.image.load("graphics/player/player_right1.png").convert_alpha(), pygame.image.load("graphics/player/player_right2.png").convert_alpha(), pygame.image.load("graphics/player/player_right3.png").convert_alpha()]
linksgehen = [pygame.image.load("graphics/player/player_left1.png").convert_alpha(), pygame.image.load("graphics/player/player_left2.png").convert_alpha(), pygame.image.load("graphics/player/player_left3.png").convert_alpha()]
forwardgehen = [pygame.image.load("graphics/player/player_forward1.png").convert_alpha(), pygame.image.load("graphics/player/player_forward2.png").convert_alpha(), pygame.image.load("graphics/player/player_forward3.png").convert_alpha()]
backwardgehen = [pygame.image.load("graphics/player/player_backward1.png").convert_alpha(), pygame.image.load("graphics/player/player_backward2.png").convert_alpha(), pygame.image.load("graphics/player/player_backward3.png").convert_alpha()]

#playerImg = pygame.image.load("graphics/zelda_test_char.png").convert_alpha()
playerX = 250
playerY = 250
playerSpeed = 5

background = pygame.image.load("graphics/test_bgImg.jpg").convert_alpha()

def textObjekt(text, pixel_font):
    textFlaeche = pixel_font.render(text, True, (0, 0, 0))
    return textFlaeche, textFlaeche.get_rect()

maus_aktiv = False
option = "Home"

def button(but_txt, but_x, but_y, but_laenge, but_hoehe, but_color_0, but_color_1):
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
            elif but_txt == "Home":
                option = "Home"
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

def infoleiste():
    pygame.draw.rect(screen, (142,255,57), (0, 1010, 1920, 80))
    button("Home",          20, 1020, 200, 50, "Red", "Green")
    button("Settings",      1700, 1020, 200, 50, "Red", "Green")

def zeichnen(liste):
    global step_rechts, step_links, step_forward, step_backward
    if step_rechts == 8:
        step_rechts = 0
    if step_links == 8:
        step_links = 0
    if step_forward == 8:
        step_forward = 0
    if step_backward == 8:
        step_backward = 0

    if player_state[0]:
        screen.blit(linksgehen[step_links // 3], (playerX,playerY))
    if player_state[1]:
        screen.blit(rechtsgehen[step_rechts // 3], (playerX,playerY))
    if player_state[2]:
        screen.blit(stehen, (playerX, playerY))
    if player_state[3]:
        screen.blit(backwardgehen[step_backward // 3], (playerX, playerY))
    if player_state[4]:
        screen.blit(forwardgehen[step_forward // 3], (playerX, playerY))

    pygame.display.update()


def level(level_val):
    if level_val == 0:
        background = pygame.image.load("graphics/lvl_text_bg.png").convert_alpha()
        screen.blit(background, (0, 0))

def player(playerImg, playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))


runtime = True

#[links, rechts, stand, backward, forward]
step_rechts = 0
step_links = 0
step_forward = 0
step_backward = 0
player_state = [0, 0, 1, 0, 0]

while runtime:

    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if pressed[pygame.K_ESCAPE] and option == "Home":
            runtime = False
        if pressed[pygame.K_ESCAPE] and option != "Home":
            option = "Home"

    #player_state = [0, 0, 1, 0, 0]
    if pressed[k_up]:
        player_state = [0, 0, 0, 0, 1]
        step_forward +=1
        playerY -= 1*playerSpeed
    if pressed[k_down]:
        player_state = [0, 0, 0, 1, 0]
        step_backward += 1
        playerY += 1*playerSpeed
    if pressed[k_left]:
        player_state = [1, 0, 0, 0, 0]
        step_links +=1
        playerX -= 1*playerSpeed
    if pressed[k_right]:
        step_rechts +=1
        player_state = [0, 1, 0, 0, 0]
        playerX += 1*playerSpeed

    if option == "Home":
        startscreen()
    elif option == "Start":
        level(level_val)
        infoleiste()
        #player(playerImg, playerX, playerY)
        pass
    elif option == "Credits":
        pass



    zeichnen(player_state)
    maus_pos = pygame.mouse.get_pos()
    maus_klick = pygame.mouse.get_pressed()
    clock.tick(fps)
    #pygame.time.wait(10)                        # 10 ms delay (wegen maus)



