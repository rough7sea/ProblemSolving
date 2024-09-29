from typing import List

class Solution:
    def isBorder(self, r, c, rows, cols) -> bool:
        return r == 0 or r == rows - 1 or c == 0 or c == cols - 1


    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        toColorSet = set()
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        steps = [(0, 1),(1, 0),(0, -1),(-1, 0)]
        originColor = grid[row][col]

        def dfs(r, c):
            visited.add((r, c))
            toColor = False
            for r_dx, c_dx in steps:
                if (
                        (r + r_dx, c + c_dx) not in visited and
                        0 <= r + r_dx <= rows - 1 and
                        0 <= c + c_dx <= cols - 1
                ):
                    if grid[r + r_dx][c + c_dx] == originColor:
                        dfs(r + r_dx, c + c_dx)
                    else:
                        toColor = True
            if toColor or self.isBorder(r, c, rows, cols):
                toColorSet.add((r, c))

        dfs(row, col)

        for r,c in toColorSet:
            grid[r][c] = color

        return grid

sol = Solution()
print(sol.colorBorder(
    grid = [
        [1,1],
        [1,2]
    ], row = 0, col = 0, color = 3))
print(sol.colorBorder(
    grid = [
        [1,2,2],
        [2,3,2]
    ], row = 0, col = 1, color = 3))

print(sol.colorBorder(
    grid = [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ], row = 1, col = 1, color = 2))
