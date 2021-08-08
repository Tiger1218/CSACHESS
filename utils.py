import pygame

BLACK = (0, 0, 0)
A_TABLE = [(x, y) for x in range(9) for y in range(10)]
R_TABLE = [(x, y) for x in range(9) for y in range(5)]
B_TABLE = [(x, y) for x in range(9) for y in range(5, 10)]
S_TABLE = {"black" : B_TABLE , "red" : R_TABLE}
B_PALACE = [(x, y) for x in range(3, 6) for y in range(3)]
R_PALACE = [(x, y) for x in range(3, 6) for y in range(7, 10)]
S_PALACE = {"black" : B_PALACE , "red" : R_PALACE}


def initPictures(chess_themes, table_themes):
    main_table = pygame.image.load("res/" + table_themes + ".gif")
    icon = pygame.image.load("res/icon.GIF")
    pictureDir = "res/" + chess_themes + "/"
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
            "black_cannon": black_cannon, "black_soldier": black_soldier, "red_rook": red_rook,
            "red_knight": red_knight, "red_bishop": red_bishop, "red_guardian": red_guardian,
            "red_king": red_king, "red_cannon": red_cannon, "red_soldier": red_soldier
            }
