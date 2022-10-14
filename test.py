import pygame
import sys
import random

pygame.display.set_caption("Zelda")
pygame.init()
screen = pygame.display.set_mode([1920, 1080])  #1920x1080
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
k_shoot = pygame.K_SPACE
last_dir = [0,0]


runtime = True

#[links, rechts, stand, backward, forward]


#playerImg = pygame.image.load("graphics/zelda_test_char.png").convert_alpha()

maus_aktiv = False
option = "Home"

stehen_links = pygame.image.load("graphics/player/player_standing_left.png").convert_alpha()
stehen_rechts = pygame.image.load("graphics/player/player_standing_right.png").convert_alpha()
rechtsgehen = [pygame.image.load("graphics/player/player_right1.png").convert_alpha(), pygame.image.load("graphics/player/player_right2.png").convert_alpha(), pygame.image.load("graphics/player/player_right3.png").convert_alpha()]
linksgehen = [pygame.image.load("graphics/player/player_left1.png").convert_alpha(), pygame.image.load("graphics/player/player_left2.png").convert_alpha(), pygame.image.load("graphics/player/player_left3.png").convert_alpha()]
forwardgehen = [pygame.image.load("graphics/player/player_forward1.png").convert_alpha(), pygame.image.load("graphics/player/player_forward2.png").convert_alpha(), pygame.image.load("graphics/player/player_forward3.png").convert_alpha()]
backwardgehen = [pygame.image.load("graphics/player/player_backward1.png").convert_alpha(), pygame.image.load("graphics/player/player_backward2.png").convert_alpha(), pygame.image.load("graphics/player/player_backward3.png").convert_alpha()]

#gras = pygame.image.load("graphics/tiles/Grass_64x64.png")
#brick = pygame.image.load("graphics/tiles/Dirt_Road_64x64.png")
#dirt = pygame.image.load("graphics/tiles/Brick_Wall_64x64.png")

background = pygame.image.load("graphics/test_bgImg.jpg").convert_alpha()

class Spieler:
    def __init__(self,playerX, playerY, playerSpeed, breite, hoehe, player_state, step_rechts, step_links, step_forward, step_backward, ok_shoot):
        self.playerX = playerX
        self.playerY = playerY
        self.playerSpeed = playerSpeed
        self.breite = breite
        self.hoehe = hoehe
        self.player_state = player_state
        self.step_rechts = step_rechts
        self.step_links = step_links
        self.step_forward = step_forward
        self.step_backward = step_backward
        self.ok_shoot = ok_shoot
        self.last_dir = last_dir

    def laufen(self, liste):
        if liste[0]:
            self.playerX -= self.playerSpeed
            self.player_state = [1, 0, 0, 0, 0]
            self.step_links += 1
        if liste[1]:
            self.playerX += self.playerSpeed
            self.player_state = [0, 1, 0, 0, 0]
            self.step_rechts += 1
        if liste[2]:
            self.playerY -= self.playerSpeed
            self.player_state = [0, 0, 0, 0, 1]
            self.step_forward += 1
        if liste[3]:
            self.playerY += self.playerSpeed
            self.player_state = [0, 0, 0, 1, 0]
            self.step_backward += 1


    def spieler_blit(self):
        if self.step_rechts == 8:
            self.step_rechts = 0
        if self.step_links == 8:
            self.step_links = 0
        if self.step_forward == 8:
            self.step_forward = 0
        if self.step_backward == 8:
            self.step_backward = 0

        if self.player_state[0]:
            screen.blit(linksgehen[self.step_links // 3], (self.playerX, self.playerY))
        if self.player_state[1]:
            screen.blit(rechtsgehen[self.step_rechts // 3], (self.playerX, self.playerY))
        if self.player_state[2]:
            if last_dir[0]:
                screen.blit(stehen_links, (self.playerX, self.playerY))
            else:
                screen.blit(stehen_rechts, (self.playerX, self.playerY))                                     #----------------------------------
        if self.player_state[3]:
            screen.blit(backwardgehen[self.step_backward // 3], (self.playerX, self.playerY))
        if self.player_state[4]:
            screen.blit(forwardgehen[self.step_forward // 3], (self.playerX, self.playerY))

    def resetSchritte(self):
        self.step_rechts = 6
        self.step_links = 6
        self.step_forward = 6
        self.step_backward = 6

    def stehen(self):
        self.player_state = [0,0,1,0,0]
        self.resetSchritte()

class kugel:
    def __init__(self, playerX, playerY, last_dir, kug_rad, kud_color, kug_speed):
        self.x = playerX
        self.y = playerY
        self.kug_speed = kug_speed
        if last_dir[0]:                                                                        # wo soll die kugel starten (links / rechts)
            self.x += 5
            self.kug_speed = -1 * kug_speed
        elif last_dir[1]:
            self.x += 75                                                                       # wo soll die kugel starten (links / rechts)
            self.kug_speed = kug_speed
        self.y += 45                                                                           # höhe des abfeuerns
        self.kug_rad = kug_rad
        self.kug_color = kud_color

    def bewegen(self):
        self.x += self.kug_speed

    def zeichnen(self):
        pygame.draw.circle(screen, self.kug_color,(self.x,self.y), self.kug_rad, 0)           # 0 am ende sagt aus ob gefüllt oder nicht

def textObjekt(text, pixel_font):
    textFlaeche = pixel_font.render(text, True, (0, 0, 0))
    return textFlaeche, textFlaeche.get_rect()
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

#def level(level_val):
    if level_val == 0:
        background = pygame.image.load("graphics/test_arena.png").convert_alpha()
        screen.blit(background, (0, 0))
def draw():

    spieler1.spieler_blit()
    for k in kugeln:
        k.zeichnen()
    pygame.display.update()

#level1 = level(0, 0, 0, 0, True)
spieler1 = Spieler(250,250, 3, 64,64,[0,0,1,0,0], 0,0,0,0, 0)
kugeln = []
spieler1.ok_shoot = True





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
        spieler1.laufen([0,0,1,0])
    if pressed[k_down]:
        spieler1.laufen([0,0,0,1])
    if pressed[k_left]:
        spieler1.laufen([1,0,0,0])
        last_dir = [1,0]
    if pressed[k_right]:
        spieler1.laufen([0,1,0,0])
        last_dir = [0,1]
    if pressed[k_up] == False and pressed[k_down] == False and pressed[k_left] == False and pressed[k_right] == False:
        spieler1.stehen()


    if option == "Home":
        startscreen()
    elif option == "Start":
        pygame.display.update()
        #level1.create_level()
        infoleiste()

    elif option == "Credits":
        pass

    if pressed[k_shoot]:
        if len(kugeln) <= 4 and spieler1.ok_shoot:  # maximale anzahl an zu schießenden Kugeln festlegen
            kugeln.append(kugel(round(spieler1.playerX), round(spieler1.playerY), last_dir, 4, (0, 0, 0), 7))
        spieler1.ok_shoot = False

    if not pressed[k_shoot]:
        spieler1.ok_shoot = True

    for k in kugeln:
        if k.x >= 0 and k.x <= 1800:
            k.bewegen()
        else:
            kugeln.remove(k)


    maus_pos = pygame.mouse.get_pos()
    maus_klick = pygame.mouse.get_pressed()
    clock.tick(60)
    draw()
    #pygame.time.wait(10)                        # 10 ms delay (wegen maus)
