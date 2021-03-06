"""
Main Activity programmed by tiger1218(tiger1218@foxmail.com) , 2021/08/07
AI Activity programmed by Accelerator(911184274@qq.com) , 2021/08/11
能把现实世界暂时抛之脑后的玩家是幸福的，每个游戏不过是一堆数据，但对有些玩家来说真的是一个美丽的虚幻世界。
"""
import time

from tkinter import messagebox
from tkinter import *
import numpy
import datetime
from utils import *
from queue import Queue
import logging


# pictureList = initPictures()
# print(pictureList['main_table'])


# class Moving:
#     def __init__(self, fpos, tpos, chessman, side):
#         self.posFrom = fpos
#         self.posTo = tpos
#         self.chessman = chessman
#         self.side = side
#
#     def format(self):
#
#
#
#
#
# class Recorder:
#     def __init__(self):
#         self.recorder = []
#
#     def add(self, move):
#         self.recorder.append(move)
#
#     def


# 棋子（所有棋子的父类）

def preMove(pos, tables):
    eat = False
    if tables[pos[0]][pos[1]] != null_chessman:
        eat = True
    return eat


class Chessman:
    def __init__(self, side, name, display, pos):
        self.side = side
        self.name = name
        self.display = display
        self.pos = pos
        self.alive = True

    def __eq__(self, other):
        return self.side == other.side and self.name == other.name and self.pos == other.pos

    def __copy__(self):
        return Chessman(side=self.side, name=self.name, display=self.display, pos=self.pos)

    def __str__(self):
        return "{0} on {1}".format(self.name, self.pos)

    def copy(self):
        return Chessman(side=self.side, name=self.name, display=self.display, pos=self.pos)

    def move(self, pos):
        if DEBUG_MODE:
            logging.info("[" + datetime.datetime.now().strftime(
                "%F%T") + "]" + str(self) + "move to " + str(pos))
        self.pos = pos

    def reachPlace(self, tables):
        # newTable = numpy.full((9, 10), null_chessman)
        reachList = []
        # for x, y in A_TABLE:
        #     newTable[x][y] = tables[x][y]
        # if self.reachPlaceB(tables) is None:
        #     return reachList
        if self.reachPlaceB(tables) is None:
            return reachList
        for reach in self.reachPlaceB(tables):
            # copyTable = newTable
            # oPos = self.pos
            # oldChess = copyTable[reach[0]][reach[1]]
            # copyTable[oPos[0]][oPos[1]] = null_chessman
            # copyTable[reach[0]][reach[1]] = self
            # if not checkmateChecking(copyTable, self.side):
            #     reachList.append(reach)
            # copyTable[oPos[0]][oPos[1]] = self
            # copyTable[reach[0]][reach[1]] = oldChess
            if not checkmateChecking(moveTable(tables, (self.pos[0], self.pos[1]), (reach[0], reach[1])), self.side):
                reachList.append(reach)

        return reachList

    # def moveChecking(self, tables, pos):
    #     newTable = self.move(tables, pos)
    #     return winnerChecking(tables)
    def reachPlaceB(self, tables):
        return []


null_chessman = Chessman("null", "null", "null", (10, 10))
DEBUG_MODE = False


# 车
class Rook(Chessman):
    def copy(self):
        return Rook(side=self.side, name=self.name, display=self.display, pos=self.pos)

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
    def copy(self):
        return Knight(side=self.side, name=self.name, display=self.display, pos=self.pos)

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
    def copy(self):
        return Bishop(side=self.side, name=self.name, display=self.display, pos=self.pos)

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
    def copy(self):
        return Guardian(side=self.side, name=self.name, display=self.display, pos=self.pos)

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
    def copy(self):
        return King(side=self.side, name=self.name, display=self.display, pos=self.pos)

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
    def copy(self):
        return Cannon(side=self.side, name=self.name, display=self.display, pos=self.pos)

    def reachPlaceB(self, tables):
        # debug
        # if self.side == "red":
        #     tableDump(tables)
        reachList = []
        flag = False
        for row in range(self.pos[0] + 1, 8 + 1):
            if tables[row][self.pos[1]] != null_chessman:
                if flag:
                    if tables[row][self.pos[1]].side != self.side:
                        reachList.append((row, self.pos[1]))
                        break
                    if tables[row][self.pos[1]].side == self.side:
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
                    if tables[row][self.pos[1]].side == self.side:
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
                    if tables[self.pos[0]][line].side == self.side:
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
                    if tables[self.pos[0]][line].side == self.side:
                        break
                else:
                    flag = True
            if not flag:
                reachList.append((self.pos[0], line))
        # reachList.remove((self.pos[0], self.pos[1]))
        return reachList


# 兵
class Soldier(Chessman):
    def copy(self):
        return Soldier(side=self.side, name=self.name, display=self.display, pos=self.pos)

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
    chessList = []
    posK = (0, 0)
    posOK = (0, 0)
    for x, y in A_TABLE:
        if tables[x][y] != null_chessman:
            if tables[x][y].side == REVERSE_S[side]:
                chessList.append(tables[x][y])
            if "king" in tables[x][y].name and tables[x][y].side == side:
                posK = (x, y)
                # print(posK)
            if "king" in tables[x][y].name and tables[x][y].side == REVERSE_S[side]:
                posOK = (x, y)
    for chessman in chessList:
        if (chessman.reachPlaceB(tables)) is None:
            pass
        elif posK in chessman.reachPlaceB(tables):
            if DEBUG_MODE:
                logging.info("[" + datetime.datetime.now().strftime(
                    "%F%T") + "]" + "checkmateChecking -> True , by " + chessman.name)
            return True
    if posK[0] == posOK[0]:
        if posK[1] < posOK[1]:
            for item in range(posK[1] + 1, posOK[1]):
                if tables[posK[0]][item] != null_chessman:
                    return False
        else:
            for item in range(posOK[1] + 1, posK[1]):
                if tables[posK[0]][item] != null_chessman:
                    return False
    else:
        return False
    if DEBUG_MODE:
        logging.info("[" + datetime.datetime.now().strftime(
            "%F%T") + "]" + "checkmateChecking -> True , by opposites")
    return True


def showVictory(side):
    # print("{0} victory !".format(side))
    Tk().wm_withdraw()
    messagebox.showinfo("showVictory()", "{0} victory !".format(side))
    exit(0)


def checkDeath(tables, side):
    for x, y in A_TABLE:
        if tables[x][y] != null_chessman:
            if tables[x][y].side == side:
                if DEBUG_MODE:
                    logging.info("[" + datetime.datetime.now().strftime("%F%T") + "]"
                                 + tables[x][y].name + " -> " + str(tables[x][y].reachPlace(tables)))
                if len(tables[x][y].reachPlace(tables)) > 0:
                    return False
    return True


def moveTable(tables, fr, to):
    chessmanList = []
    for x, y in A_TABLE:
        if tables[x][y] != null_chessman:
            newChessman = tables[x][y].copy()
            if (x, y) == fr:
                newChessman.move(to)
            if (x, y) != to:
                chessmanList.append(newChessman)
    newTable = numpy.full((9, 10), null_chessman)
    for chessman in chessmanList:
        newTable[chessman.pos[0]][chessman.pos[1]] = chessman
    return newTable


class MainGame:
    def __init__(self, chess_theme, table_theme, side="red", debug=False):
        global DEBUG_MODE
        self.side = side
        self.flips = False
        self.chess_theme = chess_theme
        self.table_theme = table_theme
        self.debug_mode = debug
        DEBUG_MODE = debug
        if DEBUG_MODE:
            logging.basicConfig(level=logging.DEBUG, filename="log.log")
        self.table = numpy.full((9, 10), null_chessman)
        self.chessman = []
        self.pictures = []
        self.circles = []
        self.initTable()
        self.flashTable()
        self.selects = Queue()
        self.recorder = Queue()
        self.states = 0
        self.checks = 0
        pygame.mixer.init()
        pygame.mixer.music.load("res/BG.mp3")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

    def flashTable(self):
        if self.debug_mode:
            logging.info("[" + datetime.datetime.now().strftime("%F%T") + "]flashTable()")
        for x, y in A_TABLE:
            self.table[x][y] = null_chessman
        for chessman in self.chessman:
            if chessman != null_chessman:
                self.table[chessman.pos[0]][chessman.pos[1]] = chessman

    def flashList(self):
        if self.debug_mode:
            logging.info("[" + datetime.datetime.now().strftime("%F%T") + "]flashList()")
        newList = []
        for x, y in A_TABLE:
            if self.table[x][y] != null_chessman:
                newList.append(self.table[x][y])
        self.chessman = newList

    def initTable(self):
        if self.debug_mode:
            logging.info("[" + datetime.datetime.now().strftime("%F%T") + "]initTable()")
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

    def judgeVictory(self):
        if checkDeath(self.table, "red"):
            showVictory("black")
        if checkDeath(self.table, "black"):
            showVictory("red")

    def showTables(self):
        if self.debug_mode:
            logging.info("[" + datetime.datetime.now().strftime("%F%T") + "]: showTables()")
        pygame.init()
        size = 521 + 300, 577  # width, height
        screen = pygame.display.set_mode(size=size)
        pygame.display.set_icon(self.pictures['icon'])
        pygame.display.set_caption(BANNER)
        while True:
            NChessman = self.eventJudge()
            self.flashTable()
            if NChessman != null_chessman:
                self.circles = [CONVERT_P(x, y) for x, y in NChessman.reachPlace(self.table)]
            screen.fill(BLACK)
            screen.blit(self.pictures["main_table"], self.pictures["main_table"].get_rect())
            for x, y in A_TABLE:
                if self.table[x][y] != null_chessman and self.table[x][y].alive:
                    chessman = self.table[x][y]
                    screen.blit(chessman.display, (6 + chessman.pos[0] * 57, 577 - (60 + chessman.pos[1] * 57)))
            for circle in self.circles:
                pygame.draw.circle(screen, BLUE, (circle[0], circle[1]), 8, 8)
            pygame.display.flip()
            self.judgeVictory()

    def humanMoving(self, side):
        if self.debug_mode:
            logging.info("[" + datetime.datetime.now().strftime("%F%T") + "]: humanMoving({})".format(side))
        pos = pygame.mouse.get_pos()
        chessPos = (round((pos[0] - 36) / 57), 9 - round((pos[1] - 28) / 57))
        # print(chessPos)
        if chessPos not in A_TABLE:
            return null_chessman
        if self.selects.empty():
            for i in range(len(self.chessman)):
                if self.chessman[i].pos == chessPos and self.chessman[i].side == side:
                    self.chessman[i].display = self.pictures[nameProcess(self.chessman[i].name) + "_select"]
                    self.selects.put(i)
                    selectSound.play()
                    return self.chessman[i]
        else:
            self.circles = []
            iNum = self.selects.get()
            self.chessman[iNum].display = self.pictures[nameProcess(self.chessman[iNum].name)]
            if chessPos not in self.chessman[iNum].reachPlace(self.table):
                return null_chessman
            else:
                eat = preMove(chessPos, self.table)
                if eat:
                    for xNum in range(len(self.chessman)):
                        if self.chessman[xNum].pos == chessPos:
                            eatSound.play()
                            self.chessman[xNum] = null_chessman
                self.chessman[iNum].move(chessPos)
                fallSound.play()
                if checkmateChecking(self.table, "red") or checkmateChecking(self.table, "black"):
                    if abs(self.checks - self.states) >= 2:
                        if DEBUG_MODE:
                            logging.info("[" + datetime.datetime.now().strftime("%F%T") + "]: playCheckmateSound()")
                        checkmateSound.play()
                        self.checks = self.states
                return Chessman(1000, 1000, 1000, 1000)
        return null_chessman

    def eventJudge(self):
        time.sleep(0.1)
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not self.selects.empty():
                    self.states = self.states + 1
                    self.side = REVERSE_S[self.side]
                    tChessman = self.humanMoving(REVERSE_S[self.side])
                    if tChessman == null_chessman:
                        self.side = REVERSE_S[self.side]
                    return null_chessman
                else:
                    self.states = self.states + 1
                    return self.humanMoving(self.side)
            else:
                if self.side == "black":
                    self.computerMoving()
                    # self.debugMoving()
                    self.states = self.states + 1
                    self.side = REVERSE_S[self.side]
        return null_chessman

    def computerMoving(self):
        if self.debug_mode:
            logging.info("[" + datetime.datetime.now().strftime("%F%T") + "]: computerMoving()")
        canary = 0
        rNum = __import__("random").randint(0, len(self.chessman) // 2)
        while len(self.chessman[rNum].reachPlace(self.table)) == 0 or self.chessman[rNum].side == "red":
            if canary > 10000:
                return
            canary = canary + 1
            rNum = __import__("random").randint(0, len(self.chessman) // 2)
        # print(self.chessman[rNum].name)
        rMov = self.chessman[rNum].reachPlace(self.table) \
            [__import__("random").randint(0, len(self.chessman[rNum].reachPlace(self.table)) - 1)]
        eat = preMove(rMov, self.table)
        if eat:
            for xNum in range(len(self.chessman)):
                if self.chessman[xNum].pos == rMov:
                    eatSound.play()
                    self.chessman[xNum] = null_chessman
        if checkmateChecking(self.table, "red") or checkmateChecking(self.table, "black"):
            if abs(self.checks - self.states) >= 2:
                if DEBUG_MODE:
                    logging.info("[" + datetime.datetime.now().strftime("%F%T") + "]: playCheckmateSound()")
                checkmateSound.play()
                self.checks = self.states
        self.chessman[rNum].move(rMov)
        # self.flashTable()

    def debugMoving(self):
        if self.debug_mode:
            logging.info("[" + datetime.datetime.now().strftime("%F%T") + "]: debugMoving()")
        posMovFrom = int(input("posMovFrom1")), int(input("posMovFrom2"))
        posMovTo = int(input("posMovTo1")), int(input("posMovTo2"))
        for iNum in range(len(self.chessman)):
            if self.chessman[iNum].pos == posMovFrom:
                eat = preMove(posMovTo, self.table)
                if eat:
                    for xNum in range(len(self.chessman)):
                        if self.chessman[xNum].pos == posMovTo:
                            self.chessman[xNum] = null_chessman
                self.chessman[iNum].move(posMovTo)
        self.flashTable()


def tableDump(tables):
    for x, y in A_TABLE:
        print(tables[x][y].name)


newGame = MainGame(chess_theme="WOOD", table_theme="WOOD", debug=False, side="red")
newGame.showTables()
