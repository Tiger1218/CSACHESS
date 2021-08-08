import pygame
import sys




def initGame():
    global pictureList
    pictureList = initPictures()
    pygame.init()
    size = width, height = 521 + 300, 577
    screen = pygame.display.set_mode(size=size)
    pygame.display.set_icon(pictureList["icon"])
    pygame.display.set_caption("雅礼中学计算机协会象棋人工智能 v0.1 by tiger1218")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        screen.fill((0, 0, 0))
        screen.blit(pictureList["main_table"], pictureList["main_table"].get_rect())
        pygame.display.flip()


# initGame()
