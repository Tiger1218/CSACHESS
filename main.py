'''
Main Activity programmed by tiger1218(tiger1218@foxmail.com) , 2021/08/07



'''
import pygame


def initPictures(themes):
    main_table = pygame.image.load("res/" + themes + ".gif")
    icon = pygame.image.load("res/icon.GIF")
    pictureDir = "res/" + themes + "/"
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


# pictureList = initPictures()
# print(pictureList['main_table'])


# 棋子（所有棋子的父类）
class Chessman:
    def __init__(self, side, name, display, pos):
        self.side = side
        self.name = name
        self.display = display
        self.pos = pos
        self.alive = True


# 车
class Rook(Chessman):
    pass


# 马
class Knight(Chessman):
    pass


# 相
class Bishop(Chessman):
    pass


# 士
class Guardian(Chessman):
    pass


# 帅
class King(Chessman):
    pass


# 炮
class Cannon(Chessman):
    pass


# 兵
class Soldier(Chessman):
    pass


# knight_pos = Position(1,1)
# knight = Chessman("black", "马", "马", (1, 1))
# print(knight.side)

class MainGame:
    def __init__(self, theme):
        self.theme = theme

    def initTable(self):
        pictureList = initPictures(self.theme)
        black_rook_left = Rook("black", "black_rook_left", pictureList["black_rook"], (8 , 9))
        black_rook_right = Rook("black", "black_rook_right", pictureList["black_rook"], (0, 9))
        black_knight_left = Knight("black", "black_knight_left", pictureList["black_knight"], (7, 9))
        black_knight_right = Knight("black", "black_knight_right", pictureList["black_knight"], (1, 9))
        black_bishop_left = Bishop("black", "black_bishop_left", pictureList["black_bishop"], (6, 9))
        black_bishop_right = Bishop("black", "black_bishop_right", pictureList["black_bishop"], (2, 9))
        black_guardian_left = Guardian("black", "black_guardian_left", pictureList["black_guardian"], (5, 9))
        black_guardian_right = Guardian("black", "black_guardian_right", pictureList["black_guardian"], (3, 9))
        black_king = King("black", "black_king", pictureList["black_king"], (4, 9))
        black_soldier_1 = Soldier("black", "black_soldier_1", pictureList["black_soldier"], (0, 6))
        black_soldier_2 = Soldier("black", "black_soldier_2", pictureList["black_soldier"], (2, 6))
        black_soldier_3 = Soldier("black", "black_soldier_3", pictureList["black_soldier"], (4, 6))
        black_soldier_4 = Soldier("black", "black_soldier_4", pictureList["black_soldier"], (6, 6))
        black_soldier_5 = Soldier("black", "black_soldier_5", pictureList["black_soldier"], (8, 6))
        red_rook_left = Rook("red", "red_rook_left", pictureList["red_rook"], (0, 0))
        red_rook_right = Rook("red", "red_rook_right", pictureList["red_rook"], (8, 0))
        red_knight_left = Knight("red", "red_knight_left", pictureList["red_knight"], (1, 0))
        red_knight_right = Knight("red", "red_knight_right", pictureList["red_knight"], (7, 0))
        red_bishop_left = Bishop("red", "red_bishop_left", pictureList["red_bishop"], (2, 0))
        red_bishop_right = Bishop("red", "red_bishop_right", pictureList["red_bishop"], (6, 0))
        red_guardian_left = Guardian("red", "red_guardian_left", pictureList["red_guardian"], (3, 0))
        red_guardian_right = Guardian("red", "red_guardian_right", pictureList["red_guardian"], (5, 0))
        red_king = King("red", "red_king", pictureList["red_king"], (4, 0))
        red_soldier_1 = Soldier("red", "red_soldier_1", pictureList["red_soldier"], (0, 3))
        red_soldier_2 = Soldier("red", "red_soldier_2", pictureList["red_soldier"], (2, 3))
        red_soldier_3 = Soldier("red", "red_soldier_3", pictureList["red_soldier"], (4, 3))
        red_soldier_4 = Soldier("red", "red_soldier_4", pictureList["red_soldier"], (6, 3))
        red_soldier_5 = Soldier("red", "red_soldier_5", pictureList["red_soldier"], (8, 3))
