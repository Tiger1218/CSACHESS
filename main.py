"""
Main Activity programmed by tiger1218(tiger1218@foxmail.com) , 2021/08/07
"""
import time

import pygame
import sys
import numpy
from utils import *
from queue import Queue

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

    def __eq__(self, other):
        return self.side == other.side and self.name == other.name and self.pos == other.pos

    def move(self, pos):
        self.pos = pos

    def reachPlace(self, tables):
        reachList = []
        for reach in self.reachPlaceB(tables):
            if not checkmateChecking(self.move(tables, reach), self.side):
                reachList.append(reach)
        return reachList

    # def moveChecking(self, tables, pos):
    #     newTable = self.move(tables, pos)
    #     return winnerChecking(tables)
    def reachPlaceB(self, tables):
        pass


null_chessman = Chessman("null", "null", "null", (0, 0))


# 车
class Rook(Chessman):
    def reachPlaceB(self, tables):
        reachList = []
        for row in range(self.pos[0] + 1, 8 + 1):
            if tables[row][self.pos[1]] != null_chessman:
                if tables[row][self.pos[1]].side != self.side:
                    reachList.append((row, self.pos[1]))
                break
            reachList.append((row, self.pos[1]))
        for row in range(self.pos[0] - 1, -1, -1):
            if tables[row][self.pos[1]] != null_chessman:
                if tables[row][self.pos[1]].side != self.side:
                    reachList.append((row, self.pos[1]))
                break
            reachList.append((row, self.pos[1]))
        for line in range(self.pos[1] + 1, 9 + 1):
            if tables[self.pos[0]][line] != null_chessman:
                if tables[self.pos[0]][line].side != self.side:
                    reachList.append((self.pos[0], line))
                break
            reachList.append((self.pos[0], line))
        for line in range(self.pos[1] - 1, -1, -1):
            if tables[self.pos[0]][line] != null_chessman:
                if tables[self.pos[0]][line].side != self.side:
                    reachList.append((self.pos[0], line))
                break
            reachList.append((self.pos[0], line))
        # reachList.remove((self.pos[0], self.pos[1]))
        return reachList


# 马
class Knight(Chessman):
    def reachPlaceB(self, tables):
        reachListx = [(self.pos[0] + 1, self.pos[1] + 2, self.pos[0], self.pos[1] + 1),
                      (self.pos[0] + 1, self.pos[1] - 2, self.pos[0], self.pos[1] - 1),
                      (self.pos[0] - 1, self.pos[1] - 2, self.pos[0], self.pos[1] - 1),
                      (self.pos[0] - 1, self.pos[1] + 2, self.pos[0], self.pos[1] + 1),
                      (self.pos[0] + 2, self.pos[1] - 1, self.pos[0] + 1, self.pos[1]),
                      (self.pos[0] + 2, self.pos[1] + 1, self.pos[0] + 1, self.pos[1]),
                      (self.pos[0] - 2, self.pos[1] - 1, self.pos[0] - 1, self.pos[1]),
                      (self.pos[0] - 2, self.pos[1] + 1, self.pos[0] - 1, self.pos[1])]
        reachList = []
        for reach in reachListx:
            if (reach[0], reach[1]) in A_TABLE:
                if (tables[reach[0]][reach[1]] == null_chessman or tables[reach[0]][reach[1]].side != self.side) \
                        and tables[reach[2]][reach[3]] == null_chessman:
                    reachList.append((reach[0], reach[1]))
        return reachList


# 相
class Bishop(Chessman):
    def reachPlaceB(self, tables):
        reachListx = [(self.pos[0] + 2, self.pos[1] + 2, self.pos[0] + 1, self.pos[1] + 1),
                      (self.pos[0] - 2, self.pos[1] + 2, self.pos[0] - 1, self.pos[1] + 1),
                      (self.pos[0] + 2, self.pos[1] - 2, self.pos[0] + 1, self.pos[1] - 1),
                      (self.pos[0] - 2, self.pos[1] - 2, self.pos[0] - 1, self.pos[1] - 1)]
        reachList = []
        for reach in reachListx:
            if (reach[0], reach[1]) in S_TABLE[self.side]:
                if (tables[reach[0]][reach[1]] == null_chessman or tables[reach[0]][reach[1]].side != self.side) \
                        and tables[reach[2]][reach[3]] == null_chessman:
                    reachList.append((reach[0], reach[1]))
        return reachList


# 士
class Guardian(Chessman):
    def reachPlaceB(self, tables):
        reachListx = [(self.pos[0] + 1, self.pos[1] + 1),
                      (self.pos[0] - 1, self.pos[1] + 1),
                      (self.pos[0] + 1, self.pos[1] - 1),
                      (self.pos[0] - 1, self.pos[1] - 1)]
        reachList = []
        for reach in reachListx:
            if reach in S_PALACE[self.side]:
                if tables[reach[0]][reach[1]].side != self.side:
                    reachList.append((reach[0], reach[1]))
        return reachList


# 帅
class King(Chessman):
    def reachPlaceB(self, tables):
        reachListx = [(self.pos[0], self.pos[1] + 1),
                      (self.pos[0] - 1, self.pos[1]),
                      (self.pos[0] + 1, self.pos[1]),
                      (self.pos[0], self.pos[1] - 1)]
        reachList = []
        for reach in reachListx:
            if reach in S_PALACE[self.side]:
                if tables[reach[0]][reach[1]].side != self.side:
                    reachList.append((reach[0], reach[1]))
        return reachList


# 炮
class Cannon(Chessman):
    def reachPlaceB(self, tables):
        reachList = []
        flag = False
        for row in range(self.pos[0] + 1, 8 + 1):
            if tables[row][self.pos[1]] != null_chessman:
                if flag:
                    if tables[row][self.pos[1]].side != self.side:
                        reachList.append((row, self.pos[1]))
                        break
                else:
                    flag = True
            if not flag:
                reachList.append((row, self.pos[1]))
        flag = False
        for row in range(self.pos[0] - 1, -1, -1):
            if tables[row][self.pos[1]] != null_chessman:
                if flag:
                    if tables[row][self.pos[1]].side != self.side:
                        reachList.append((row, self.pos[1]))
                        break
                else:
                    flag = True
            if not flag:
                reachList.append((row, self.pos[1]))
        flag = False
        for line in range(self.pos[1] + 1, 9 + 1):
            if tables[self.pos[0]][line] != null_chessman:
                if flag:
                    if tables[self.pos[0]][line].side != self.side:
                        reachList.append((self.pos[0], line))
                        break
                else:
                    flag = True
            if not flag:
                reachList.append((self.pos[0], line))
        flag = False
        for line in range(self.pos[1] - 1, -1, -1):
            if tables[self.pos[0]][line] != null_chessman:
                if flag:
                    if tables[self.pos[0]][line].side != self.side:
                        reachList.append((self.pos[0], line))
                        break
                else:
                    flag = True
            if not flag:
                reachList.append((self.pos[0], line))
        # reachList.remove((self.pos[0], self.pos[1]))
        return reachList


# 兵
class Soldier(Chessman):
    def reachPlaceB(self, tables):
        reachList = []
        if (self.pos[0], self.pos[1]) in S_TABLE[self.side]:
            if tables[self.pos[0]][self.pos[1] + S_FORWARD[self.side]].side != self.side:
                reachList.append((self.pos[0], self.pos[1] + S_FORWARD[self.side]))
                return reachList
        else:
            reachListx = [(self.pos[0], self.pos[1] + S_FORWARD[self.side]),
                          (self.pos[0] - 1, self.pos[1]),
                          (self.pos[0] + 1, self.pos[1])]
            for reach in reachListx:
                if reach in A_TABLE:
                    if tables[reach[0]][reach[1]].side != self.side:
                        reachList.append((reach[0], reach[1]))
            return reachList


def checkmateChecking(tables, side):
    red_king_pos = (0, 0)
    for x, y in S_PALACE[side]:
        if tables[x][y].name == side + "_king":
            red_king_pos = (x, y)
    for x, y in A_TABLE:
        if tables[x][y].side == REVERSE_S[side]:
            if red_king_pos in tables[x][y].reachPlaceB(tables):
                return True
    return False


# knight_pos = Position(1,1)
# knight = Chessman("black", "马", "马", (1, 1))
# print(knight.side)

class MainGame:
    def __init__(self, chess_theme, table_theme, side = "red"):
        self.side = side
        self.flips = False
        self.chess_theme = chess_theme
        self.table_theme = table_theme
        self.table = numpy.full((9, 10), null_chessman)
        self.chessman = []
        self.pictures = []
        self.circles = []
        self.initTable()
        self.flashTable()
        self.selects = Queue()

    def flashTable(self):
        for chessman in self.chessman:
            self.table[chessman.pos[0]][chessman.pos[1]] = chessman

    def initTable(self):
        # 初始化棋子和棋子的位置
        self.pictures = initPictures(self.chess_theme, self.table_theme)
        self.chessman = [Rook("black", "black_rook_left", self.pictures["black_rook"], (8, 9)),
                         Rook("black", "black_rook_right", self.pictures["black_rook"], (0, 9)),
                         Knight("black", "black_knight_left", self.pictures["black_knight"], (7, 9)),
                         Knight("black", "black_knight_right", self.pictures["black_knight"], (1, 9)),
                         Bishop("black", "black_bishop_left", self.pictures["black_bishop"], (6, 9)),
                         Bishop("black", "black_bishop_right", self.pictures["black_bishop"], (2, 9)),
                         Guardian("black", "black_guardian_left", self.pictures["black_guardian"], (5, 9)),
                         Guardian("black", "black_guardian_right", self.pictures["black_guardian"], (3, 9)),
                         King("black", "black_king_", self.pictures["black_king"], (4, 9)),
                         Cannon("black", "black_cannon_left", self.pictures["black_cannon"], (7, 7)),
                         Cannon("black", "black_cannon_right", self.pictures["black_cannon"], (1, 7)),
                         Soldier("black", "black_soldier_1", self.pictures["black_soldier"], (0, 6)),
                         Soldier("black", "black_soldier_2", self.pictures["black_soldier"], (2, 6)),
                         Soldier("black", "black_soldier_3", self.pictures["black_soldier"], (4, 6)),
                         Soldier("black", "black_soldier_4", self.pictures["black_soldier"], (6, 6)),
                         Soldier("black", "black_soldier_5", self.pictures["black_soldier"], (8, 6)),
                         Rook("red", "red_rook_left", self.pictures["red_rook"], (0, 0)),
                         Rook("red", "red_rook_right", self.pictures["red_rook"], (8, 0)),
                         Knight("red", "red_knight_left", self.pictures["red_knight"], (1, 0)),
                         Knight("red", "red_knight_right", self.pictures["red_knight"], (7, 0)),
                         Bishop("red", "red_bishop_left", self.pictures["red_bishop"], (2, 0)),
                         Bishop("red", "red_bishop_right", self.pictures["red_bishop"], (6, 0)),
                         Guardian("red", "red_guardian_left", self.pictures["red_guardian"], (3, 0)),
                         Guardian("red", "red_guardian_right", self.pictures["red_guardian"], (5, 0)),
                         King("red", "red_king_", self.pictures["red_king"], (4, 0)),
                         Cannon("red", "red_cannon_left", self.pictures["red_cannon"], (1, 2)),
                         Cannon("red", "red_cannon_right", self.pictures["red_cannon"], (7, 2)),
                         Soldier("red", "red_soldier_1", self.pictures["red_soldier"], (0, 3)),
                         Soldier("red", "red_soldier_2", self.pictures["red_soldier"], (2, 3)),
                         Soldier("red", "red_soldier_3", self.pictures["red_soldier"], (4, 3)),
                         Soldier("red", "red_soldier_4", self.pictures["red_soldier"], (6, 3)),
                         Soldier("red", "red_soldier_5", self.pictures["red_soldier"], (8, 3))]

    def showTables(self):
        pygame.init()
        size = width, height = 521 + 300, 577
        screen = pygame.display.set_mode(size=size)
        pygame.display.set_icon(self.pictures["icon"])
        pygame.display.set_caption("雅礼中学计算机协会象棋人工智能 v0.1 by tiger1218")
        while True:
            NChessman = self.eventJudge()
            self.flashTable()
            if NChessman != null_chessman:
                self.circles = [CONVERT_P(x, y) for x, y in NChessman.reachPlaceB(self.table)]
            screen.fill(BLACK)
            screen.blit(self.pictures["main_table"], self.pictures["main_table"].get_rect())
            for x, y in A_TABLE:
                if self.table[x][y] != null_chessman:
                    chessman = self.table[x][y]
                    screen.blit(chessman.display, (6 + chessman.pos[0] * 57, 577 - (60 + chessman.pos[1] * 57)))
            for circle in self.circles:
                pygame.draw.circle(screen, BLUE, (circle[0], circle[1]), 8, 8)
            pygame.display.flip()

    def eventJudge(self):
        time.sleep(0.1)
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                chessPos = (round((pos[0] - 36) / 57), 9 - round((pos[1] - 28) / 57))
                if chessPos not in A_TABLE:
                    return null_chessman
                if self.selects.empty():
                    for i in range(len(self.chessman)):
                        if self.chessman[i].pos == chessPos:
                            self.chessman[i].display = self.pictures[nameProcess(self.chessman[i].name) + "_select"]
                            self.selects.put(i)
                            return self.chessman[i]
                else:
                    # print("MOVEING")
                    self.circles = []
                    iNum = self.selects.get()
                    self.chessman[iNum].display = self.pictures[nameProcess(self.chessman[iNum].name)]
                    if chessPos not in self.chessman[iNum].reachPlaceB(self.table):
                        return null_chessman
                    else:
                        self.chessman[iNum].move(chessPos)


        return null_chessman


newGame = MainGame("WOOD", "WOOD")
newGame.showTables()
