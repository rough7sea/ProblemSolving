from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int,
                       guards: List[List[int]], walls: List[List[int]]) -> int:

        res = m * n - len(walls) - len(guards)
        if res == 0:
            return 0

        grid = [[None for i in range(n)] for j in range(m)]
        for wall in walls:
            i, j = wall
            grid[i][j] = 'w'
        for guard in guards:
            i, j = guard
            grid[i][j] = 'g'

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 'g':
                    continue
                for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    next_i = i + di
                    next_j = j + dj
                    while 0 <= next_i < m and 0 <= next_j < n:
                        if grid[next_i][next_j] == 'w' or grid[next_i][next_j] == 'g':
                            break
                        if grid[next_i][next_j] is None:
                            res -= 1
                        grid[next_i][next_j] = 1
                        next_i += di
                        next_j += dj
        # print(grid)

        return res


sol = Solution()
print(sol.countUnguarded(m=4, n=6, guards=[[0, 0], [1, 1], [2, 3]], walls=[[0, 1], [2, 2], [1, 4]]))
