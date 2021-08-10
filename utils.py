import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
A_TABLE = [(x, y) for x in range(9) for y in range(10)]
R_TABLE = [(x, y) for x in range(9) for y in range(5)]
B_TABLE = [(x, y) for x in range(9) for y in range(5, 10)]
S_TABLE = {"black": B_TABLE, "red": R_TABLE}
B_PALACE = [(x, y) for x in range(3, 6) for y in range(7, 10)]
R_PALACE = [(x, y) for x in range(3, 6) for y in range(3)]
S_PALACE = {"black": B_PALACE, "red": R_PALACE}
S_FORWARD = {"black": -1, "red": 1}
REVERSE_S = {"black": "red", "red": "black"}
DEBUG_MODE = False


def CONVERT_P(x, y):
    return 34 + x * 57, (9 - y) * 57 + 31


def nameProcess(string):
    return string[0:string.rfind('_')]


def initPictures(chess_themes, table_themes):
    main_table = pygame.image.load("res/" + table_themes + ".gif")
    icon = pygame.image.load("res/icon.GIF")
    pictureDir = "res/" + chess_themes + "/"
    black_rook = pygame.image.load(pictureDir + "BR.GIF")
    black_rook_select = pygame.image.load(pictureDir + "BRS.GIF")
    black_knight = pygame.image.load(pictureDir + "BKN.GIF")
    black_knight_select = pygame.image.load(pictureDir + "BKNS.GIF")
    black_bishop = pygame.image.load(pictureDir + "BB.GIF")
    black_bishop_select = pygame.image.load(pictureDir + "BBS.GIF")
    black_guardian = pygame.image.load(pictureDir + "BG.GIF")
    black_guardian_select = pygame.image.load(pictureDir + "BGS.GIF")
    black_king = pygame.image.load(pictureDir + "BK.GIF")
    black_king_select = pygame.image.load(pictureDir + "BKS.GIF")
    black_cannon = pygame.image.load(pictureDir + "BC.GIF")
    black_cannon_select = pygame.image.load(pictureDir + "BCS.GIF")
    black_soldier = pygame.image.load(pictureDir + "BS.GIF")
    black_soldier_select = pygame.image.load(pictureDir + "BSS.GIF")
    red_rook = pygame.image.load(pictureDir + "RR.GIF")
    red_rook_select = pygame.image.load(pictureDir + "RRS.GIF")
    red_knight = pygame.image.load(pictureDir + "RKN.GIF")
    red_knight_select = pygame.image.load(pictureDir + "RKNS.GIF")
    red_bishop = pygame.image.load(pictureDir + "RB.GIF")
    red_bishop_select = pygame.image.load(pictureDir + "RBS.GIF")
    red_guardian = pygame.image.load(pictureDir + "RG.GIF")
    red_guardian_select = pygame.image.load(pictureDir + "RGS.GIF")
    red_king = pygame.image.load(pictureDir + "RK.GIF")
    red_king_select = pygame.image.load(pictureDir + "RKS.GIF")
    red_cannon = pygame.image.load(pictureDir + "RC.GIF")
    red_cannon_select = pygame.image.load(pictureDir + "RCS.GIF")
    red_soldier = pygame.image.load(pictureDir + "RS.GIF")
    red_soldier_select = pygame.image.load(pictureDir + "RSS.GIF")

    return {"main_table": main_table, "icon": icon, "black_rook": black_rook, "black_knight": black_knight,
            "black_bishop": black_bishop, "black_guardian": black_guardian, "black_king": black_king,
            "black_cannon": black_cannon, "black_soldier": black_soldier, "red_rook": red_rook,
            "red_knight": red_knight, "red_bishop": red_bishop, "red_guardian": red_guardian,
            "red_king": red_king, "red_cannon": red_cannon, "red_soldier": red_soldier,
            "black_rook_select": black_rook_select, "black_knight_select": black_knight_select,
            "black_bishop_select": black_bishop_select, "black_guardian_select": black_guardian_select,
            "black_king_select": black_king_select, "black_cannon_select": black_cannon_select,
            "black_soldier_select": black_soldier_select, "red_rook_select": red_rook_select,
            "red_knight_select": red_knight_select, "red_bishop_select": red_bishop_select,
            "red_guardian_select": red_guardian_select, "red_king_select": red_king_select,
            "red_cannon_select": red_cannon_select, "red_soldier_select": red_soldier_select
            }
