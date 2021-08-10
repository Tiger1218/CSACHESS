# CSACHESS
### How to use?

```bash
pip install -r requirements.txt
python main.py
```

### Documents ?

#### class Chessman:（棋子）

* 属性side："red"或"black"，描述当前棋子的归属
* 属性name：描述棋子的名字，一般用于debug，程序中很少有用到
* 属性display：棋子的图像，初始化中已初始化
* **属性pos：棋子的位置，返回一个二元tuple(x,y)**
* 方法move：移动棋子，参数为二元tuple(x,y)，无返回值
* 方法reachPlaceB：参数为一个表，返回值为一个list，中间包含所有该棋子目前可到的位置，没考虑了将军，面将（同样为二元tuple）
* 方法reachPlace：参数为一个表，返回值为一个list，中间包含所有该棋子目前可到的位置，考虑了将军，面将（同样为二元tuple）

#### class MainGame：（游戏）

* 属性side："red"或"black"，描述当前游戏玩家为"red"或"black"
* 属性table：一个二维数组，每一个数组值都是一个chessman对象，在方法initTable()中被初始化
* 属性chessman：一个列表，储存了所有棋子
* 方法flashTable：通过属性chessman更新属性table
* 方法flashList：通过属性table更新属性chessman
* 方法computerMoving：电脑移动，也就是你要完成的内容，凭借属性table，调用chessman中的move方法，不用返回值
* 方法debugMoving：debug时使用，可以任意移动走子

#### static函数：

* checkmateChecking：参数是tables和side，返回在当前tables下，side方的王有没有被将着。True为有，False为没有
* checkDeath：参数是tables和side，返回在当前tables下，side方的王有没有被将死。有则返回True，没有则返回False
* moveTable：参数是tables、posFrom和posTo，返回将posFrom位置的棋子移动到posTo位置后的棋盘tables状态

#### 重要的常数

* null_chessman：在tables中出现null_chessman为空，那个地方没有棋子的意思
* A_TABLES：所有棋盘上的点的集合（(0,0)...一直到(8,9)）
* R_TABLES：red方点的集合
* B_TABLES：black方点的集合
* S_TABLES：S_TABLES["red"] = R_TABLES，S_TABLES["black"] = B_TABLES
* REVERSE_S：REVERSE_S["red"] = "black" , REVERSE_S["black"] = "red"

请重构class MainGame中的computerMoving()函数。
