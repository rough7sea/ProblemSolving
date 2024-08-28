from typing import List


class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     stack = []
    #     steps = [(0, 1),(1, 0),(0, -1),(-1, 0)]
    #     res = 0
    #     for i in range(len(grid)):
    #         for j in range(len(grid[i])):
    #             if grid[i][j] == '0':
    #                 continue
    #
    #             res += 1
    #             stack.append((i, j))
    #             while len(stack) > 0:
    #                 (x, y) = stack.pop()
    #                 grid[x][y] = '0'
    #                 for dx, dy in steps:
    #                     if (0 <= x + dx < len(grid)
    #                             and 0 <= y + dy < len(grid[0])
    #                             and grid[x + dx][y + dy] != '0'):
    #                         stack.append((x + dx, y + dy))
    #
    #     return res

    def numIslandsDfs(self, grid: List[List[str]]) -> int:
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0

        def rec(x, y):
            grid[x][y] = '0'
            for dx, dy in steps:
                if (0 <= x + dx < len(grid)
                        and 0 <= y + dy < len(grid[0])
                        and grid[x + dx][y + dy] != '0'):
                    rec(x + dx, y + dy)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    res += 1
                    rec(i, j)

        return res


sol = Solution()
# print(sol.numIslands(
#     grid=[
#         ["1", "1", "1", "1", "0"],
#         ["1", "1", "0", "1", "0"],
#         ["1", "1", "0", "0", "0"],
#         ["0", "0", "0", "1", "1"]
#     ]
# ))

print(sol.numIslandsDfs(
    grid=[
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
))
