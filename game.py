import pygame
import math
import random

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

xpos = 640
ypos = 360
speed = 7
scale = 1

while running:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    screen.fill("white")

    
    kboard = pygame.key.get_pressed()
    xdirect = 0
    ydirect = 0
    if kboard[pygame.K_w]:
        ydirect = -1
    if kboard[pygame.K_s]:
        ydirect = 1
    if kboard[pygame.K_a]:
        xdirect = -1
    if kboard[pygame.K_d]:
        xdirect = 1
    

    xpos = (xpos + (speed * xdirect))
    ypos = (ypos + (speed * ydirect))

    sboxsize = 50 * scale

    
    """
    if xpos > 1280:
        xpos = 1280 - sboxsize / 2
    if xpos < 0:
        xpos = 0 + sboxsize / 2
    if ypos > 720:
        ypos = 720 - sboxsize / 2
    if ypos < 0:
        ypos = 0 + sboxsize / 2
    """


    shitbox = pygame.Rect(xpos-25,ypos-25,sboxsize,sboxsize)

    button = pygame.Rect(1100, 360, scale * 50,scale * 50)
    if button.colliderect(shitbox):
        buttcolor = "red"
    else: buttcolor = "black"

    pygame.draw.rect(screen, buttcolor, button)
    pygame.draw.rect(screen, 'black', shitbox)

    pygame.display.flip()

    clock.tick(60)