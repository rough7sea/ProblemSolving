from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x,y = 0, 0
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curDirection = 0
        obstaclesMap = dict()
        maxPoint = 0
        for obstacle in obstacles:
            obstaclesMap[(obstacle[0],obstacle[1])] = True
        for com in commands:
            if com > 0:
                dx,dy = steps[curDirection]
                for i in range(com):
                    if (x + dx, y + dy) in obstaclesMap:
                        maxPoint = max(maxPoint, x ** 2 + y ** 2)
                        break
                    x += dx
                    y += dy
                maxPoint = max(maxPoint, x ** 2 + y ** 2)
            elif com == -1:
                curDirection = (curDirection + 1) % len(steps)
            elif com == -2:
                if curDirection - 1 < 0:
                    curDirection = len(steps) - 1
                else:
                    curDirection -= 1
        return maxPoint

sol = Solution()
# print(sol.robotSim(commands = [4,-1,4,-2,4], obstacles = [[2,4]]))
# print(sol.robotSim(commands = [6,-1,-1,6], obstacles = []))
print(sol.robotSim(commands = [-2,-1,8,9,6], obstacles = []))
