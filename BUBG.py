import pygame
pygame.init()
screen =pygame.display.set_mode([800, 600])
keep_going = True
pic = pygame.image.load("BUBG.jpg")
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    screen.blit(pic,(100,100))
    pygame.display.update()
pygame.quit()
input("dffcefc ecgugcrfg cvlgicvrfc fkcf f v fgv vcrfgvcfg ")