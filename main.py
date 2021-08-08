'''
Main Activity programmed by tiger1218(tiger1218@foxmail.com) , 2021/08/07



'''


# 棋子（所有棋子的父类）
class Chessman:
    def __init__(self, side, name, display, pos):
        self.side = side
        self.name = name
        self.display = display
        self.pos = pos


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
