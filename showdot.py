import pygame
import time

pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True
GREEN = (0,255,0) # RGB color triplet for GREEN
BLACK = (0, 0, 0)
radius = 50

xcoordinate = 100
ycoordinate = 100

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    pygame.draw.circle(screen, GREEN, (xcoordinate, ycoordinate), radius)
    pygame.display.update()
    time.sleep(1)
    pygame.draw.circle(screen, BLACK, (xcoordinate, ycoordinate), radius)
    pygame.display.update()

    xcoordinate += 10
    ycoordinate += 10

    if (xcoordinate == 800):
        xcoordinate = 100
    if (ycoordinate == 600):
        ycoordinate = 100

    
pygame.quit()