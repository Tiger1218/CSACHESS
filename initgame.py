import pygame
import sys

pictureList = {}
THEMES = "WOOD"


def initPictures():
    main_table = pygame.image.load("res/" + THEMES + ".gif")
    icon = pygame.image.load("res/icon.GIF")
    pictureDir = "res/" + THEMES + "/"
    black_rook = pygame.image.load(pictureDir + "BR.GIF")
    black_knight = pygame.image.load(pictureDir + "BKN.GIF")
    black_bishop = pygame.image.load(pictureDir + "BB.GIF")
    black_guardian = pygame.image.load(pictureDir + "BG.GIF")
    black_king = pygame.image.load(pictureDir + "BK.GIF")
    black_cannon = pygame.image.load(pictureDir + "BC.GIF")
    black_soldier = pygame.image.load(pictureDir + "BS.GIF")
    red_rook = pygame.image.load(pictureDir + "RR.GIF")
    red_knight = pygame.image.load(pictureDir + "RKN.GIF")
    red_bishop = pygame.image.load(pictureDir + "RB.GIF")
    red_guardian = pygame.image.load(pictureDir + "RG.GIF")
    red_king = pygame.image.load(pictureDir + "RK.GIF")
    red_cannon = pygame.image.load(pictureDir + "RC.GIF")
    red_soldier = pygame.image.load(pictureDir + "RS.GIF")

    return {"main_table": main_table, "icon": icon, "black_rook": black_rook, "black_knight": black_knight,
            "black_bishop": black_bishop, "black_guardian": black_guardian, "black_king": black_king,
            "black_cannon": black_cannon, "black_soldier": black_soldier, "red_rook": red_rook, "red_knight": red_knight, "red_bishop": red_bishop, "red_guardian": red_guardian,
            "red_king": red_king, "red_cannon": red_cannon, "red_soldier": red_soldier
            }


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


initGame()
