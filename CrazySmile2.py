import pygame
pygame.init()

screen = pygame.display.set_mode([800,600])
pic = pygame.image.load("CrazySmile.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)

BLACK = (0,0,0)
timer = pygame.time.Clock()

picx = 0
picy = 0
speedx = 11
speedy = 11

keep_going = True
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    picx += speedx
    picy += speedy

    if picx <= 0 or 800 <= picx + pic.get_width():
        speedx = -speedx

    if picy <= 0 or 600 <= picy + pic.get_height():
        speedy = -speedy

    #screen.fill(BLACK)
    screen.blit(pic, (picx, picy))
    pygame.display.update()
    timer.tick(20)

pygame.quit ()

