from typing import List


# 1 representing the starting square. There is exactly one starting square.
# 2 representing the ending square. There is exactly one ending square.
# 0 representing empty squares we can walk over.
# -1 representing obstacles that we cannot walk over.

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = None
        obstacles = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    obstacles += 1

                if grid[i][j] == 1:
                    start = [i, j]

        pathLength = len(grid) * len(grid[0]) - obstacles
        count = 0

        def findPath(prevSteps: dict, i, j):
            nonlocal count
            cur = grid[i][j]
            if cur == 2:
                print(prevSteps)
                pathLen = len(prevSteps)
                if pathLen == pathLength:
                    count += 1
                return

            for step in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                next_i = i + step[0]
                next_j = j + step[1]
                if (0 > next_i or next_i >= len(grid)
                        or 0 > next_j or next_j >= len(grid[0])
                        or grid[next_i][next_j] == -1
                        or f'{next_i} {next_j}' in prevSteps):
                    continue
                nextSteps = prevSteps.copy()
                nextSteps[f'{next_i} {next_j}'] = f'{i} {j}'
                findPath(nextSteps, next_i, next_j)

        init = dict()
        init[f'{start[0]} {start[1]}'] = f'{start[0]} {start[1]}'
        findPath(init, start[0], start[1])
        return count
    # def uniquePathsIII(self, grid: List[List[int]]) -> int:
    #     start = None
    #     obstacles = 0
    #
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if grid[i][j] == -1:
    #                 obstacles += 1
    #
    #             if grid[i][j] == 1:
    #                 start = [i, j]
    #
    #     pathLength = len(grid) * len(grid[0]) - obstacles
    #     count = 0
    #
    #     def findPath(steps, i, j):
    #         nonlocal count
    #         nonlocal pathLength
    #         if grid[i][j] == 2:
    #             if steps == pathLength:
    #                 count += 1
    #             return
    #
    #         temp = grid[i][j]
    #         grid[i][j] = -1
    #
    #         for step in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
    #             next_i = i + step[0]
    #             next_j = j + step[1]
    #             if (0 > next_i or next_i >= len(grid)
    #                     or 0 > next_j or next_j >= len(grid[0])
    #                     or grid[next_i][next_j] == -1):
    #                 continue
    #
    #             findPath(steps + 1, next_i, next_j)
    #
    #         grid[i][j] = temp
    #
    #     findPath(0, start[0], start[1])
    #     return count


sol = Solution()
print(sol.uniquePathsIII(grid=[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
print(sol.uniquePathsIII(grid=[[0, 1], [2, 0]]))
