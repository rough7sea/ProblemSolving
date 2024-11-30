from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = [[False] * m for _ in range(n)]
        visited[0][0] = True
        if not (m > 1 and grid[0][1] < 2 or n > 1 and grid[1][0] < 2):
            return -1

        queue = [(0, 0, 0)]

        while queue:
            w, i, j = heappop(queue)
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_i = i + di
                next_j = j + dj
                if (
                        0 <= next_i < n
                        and 0 <= next_j < m
                        and not visited[next_i][next_j]
                ):
                    next_grid_w = grid[next_i][next_j]
                    if w >= next_grid_w:
                        next_w = w + 1
                    else:
                        diff = next_grid_w - w
                        if diff % 2 == 0:
                            diff += 1
                        next_w = w + diff

                    if next_i == n - 1 and next_j == m - 1:
                        return next_w
                    visited[next_i][next_j] = True
                    heappush(queue, (next_w, next_i, next_j))
        return -1


sol = Solution()
print(sol.minimumTime(grid=[
    [0, 1, 3, 2],
    [5, 1, 2, 5],
    [4, 3, 8, 6]
]))
print(sol.minimumTime(grid=[[0, 2, 4], [3, 2, 1], [1, 0, 4]]))