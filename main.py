'''
Main Activity programmed by tiger1218(tiger1218@foxmail.com) , 2021/08/07



'''
class Position:
    def __init__(self , x , y):
        self.x = x
        self.y = y


class Chessman:
    def __init__(self , side , name , display , pos):
        self.side = side
        self.name = name
        self.display = display
        self.pos = pos
    def moves(self , npos):
        self.pos = npos

# knight_pos = Position(1,1)
knight = Chessman("black" , "马" , "马" , (1,1))
print(knight.side)