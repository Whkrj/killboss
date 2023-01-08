import pygame
import random
pygame.init()

screen_width = 1290
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('보스 잡기')

background = pygame.image.load('bgbg.png')
chd = pygame.image.load('chd1.png')
chd = pygame.transform.scale(chd, (300,300))
chd1 = pygame.image.load('chd1.png')
chd1 = pygame.transform.scale(chd1, (300,300))
chd2 = pygame.image.load('chd2.png')
chd2 = pygame.transform.scale(chd2, (1050,300))
ghkf = pygame.image.load('ghkf1.png')
ghkf = pygame.transform.scale(ghkf, (300,300))
ghkf1 = pygame.image.load('ghkf1.png')
ghkf1 = pygame.transform.scale(ghkf1, (300,300))
ghkf2 = pygame.image.load('ghkf2.png')
ghkf2 = pygame.transform.scale(ghkf2, (1050,300))
qhtm = pygame.image.load('qhtm.png')
qhtm = pygame.transform.scale(qhtm, (600,600))
qhtm1 = pygame.image.load('qhtm.png')
qhtm1 = pygame.transform.scale(qhtm1, (600,600))
qhtm2 = pygame.image.load('qhtm2.png')
qhtm2 = pygame.transform.scale(qhtm2, (600,600))
qhtm3 = pygame.image.load('qhtm3.png')
qhtm3 = pygame.transform.scale(qhtm3, (600,600))

hp = 200000000

runing = True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RSHIFT:
                hp -= random.randint(500000,1500000)
                chd = chd2
                qhtm = qhtm2
            if event.key == pygame.K_LSHIFT:
                hp -= random.randint(0,2000000)
                ghkf = ghkf2
                qhtm = qhtm2
        if event.type == pygame.KEYUP:
            chd = chd1
            ghkf= ghkf1
            qhtm = qhtm1
        
    screen.blit(background, (0,0))
    screen.blit(qhtm, (700,70))
    screen.blit(chd, (100,350))
    screen.blit(ghkf, (10,300))

    myFont = pygame.font.SysFont("Arial", 30, True, False)
    text_point = myFont.render("BOSS HP: " + str(hp), True, (255,255,255))
    screen.blit(text_point, (850,30))
    myFont2 = pygame.font.SysFont("Arial", 30, True, False)
    text_point2 = myFont2.render("CLEAR", True, (0,255,255))
    text_point2 = pygame.transform.scale(text_point2, (700,400))

    if hp <= 0:
        screen.blit(text_point2, (270,150))
        hp = 0
        qhtm = qhtm3


    pygame.display.update()

pygame.quit()