from typing import List


class Robot:

    def __init__(self, width: int, height: int):
        self.width = width  # x
        self.height = height  # y
        self.fullCircle = (width + height) * 2 - 4
        self.x = 0
        self.y = 0
        self.steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.dir = ["East", "North", "West", "South"]
        self.curDirection = 0

    def step(self, num: int) -> None:
        dy, dx = self.steps[self.curDirection]
        num = num % self.fullCircle

        if num == 0:
            if not (0 <= self.x - dx < self.width and 0 <= self.y - dy < self.height):
                self.curDirection -= 1
                if self.curDirection < 0:
                    self.curDirection = len(self.steps) - 1

        for i in range(num % (self.width * self.height)):
            if 0 <= self.x + dx < self.width and 0 <= self.y + dy < self.height:
                self.x += dx
                self.y += dy
            else:
                while not (0 <= self.x + dx < self.width and 0 <= self.y + dy < self.height):
                    self.curDirection = (self.curDirection + 1) % len(self.steps)
                    dy, dx = self.steps[self.curDirection]
                self.x += dx
                self.y += dy

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.dir[self.curDirection]

# r = Robot(97, 98)
# print(r.getDir())
# r.step(66392)
# print(r.getDir())
# r.step(83376)
# print(r.getDir())
# r.step(71796)
# print(r.getDir())
# r.step(57514)
# print(r.getDir())
# r.step(36284)
# print(r.getDir())
# r.step(69866)
# print(r.getDir())
# r.step(31652)
# print(r.getDir())
# r.step(32038)
# print(r.getDir())
# print(r.getPos())
# # 0, 0
#
# r.step(88780)
# print(r.getDir())
# print(r.getPos())
# [66392],[83376],[71796],[57514],[36284],[69866],[31652],[32038]
# [[97,98],[],[],[66392],[83376],[71796],[57514],[36284],[69866],[31652],[32038],[]



# [[3,3],
# [27],[47],[27],[30],[],[],
r = Robot(3, 3)
r.step(27)
r.step(47)
r.step(27)
r.step(30)
print(r.getPos())
print(r.getDir())

# [50],[],[],
r.step(50)
print(r.getPos())
print(r.getDir())

# [37],[33],[47],[47],[42],
r.step(37)
r.step(33)
r.step(47)
r.step(47)
r.step(42)
print(r.getPos())
print(r.getDir())

# [49],[25],[],[],
r.step(49)
r.step(25)
print(r.getPos())
print(r.getDir())

# [24],[19],[3],[15],[],[],
r.step(24)
r.step(19)
r.step(3)
r.step(15)
print(r.getPos())
print(r.getDir())

# [22],[17],[6],[47],[1],[],[],
r.step(22)
r.step(17)
r.step(6)
r.step(47)
r.step(1)
print(r.getPos())
print(r.getDir())

# [12],[50],[46],[34],[16],[],[],
r.step(12)
r.step(50)
r.step(46)
r.step(34)
r.step(16)
print(r.getPos())
print(r.getDir())

# [null,null,null,null,null,
# [2,1],"North",null,
# [1,2],"West",null,null,null,null,null,
# [2,1],"North",null,null,
# [1,2],"West",null,null,null,null,
# [2,0],"East",null,null,null,null,null,
# [0,1],"South",null,null,null,null,null,
# [1,2],"West",null,null,null]