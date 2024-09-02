from typing import List

steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def aroundTheIsland(x, y):
            grid2[x][y] = 0
            count = 1
            if grid1[x][y] == 0:
                count = 0
            for dx, dy in steps:
                if (
                        0 <= x + dx < len(grid2) and
                        0 <= y + dy < len(grid2[x]) and
                        grid2[x + dx][y + dy] != 0):
                    count &= aroundTheIsland(x + dx, y + dy)
            return count

        res = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[i])):
                if grid2[i][j] == 1:
                    res += aroundTheIsland(i, j)

        return res

sol = Solution()
print(sol.countSubIslands(
    grid1 = [
        [1,1,1,0,0],
        [0,1,1,1,1],
        [0,0,0,0,0],
        [1,0,0,0,0],
        [1,1,0,1,1]
    ],
    grid2 = [
        [1,1,1,0,0],
        [0,0,1,1,1],
        [0,1,0,0,0],
        [1,0,1,1,0],
        [0,1,0,1,0]
    ]
))

print(sol.countSubIslands(
    grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
))