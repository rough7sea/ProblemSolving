from heapq import heappush, heappop
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        grid = moveTime
        n = len(grid)
        m = len(grid[0])

        visited = [[False] * m for _ in range(n)]
        visited[0][0] = True

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
                        next_w = next_grid_w + 1

                    if next_i == n - 1 and next_j == m - 1:
                        return next_w
                    visited[next_i][next_j] = True
                    heappush(queue, (next_w, next_i, next_j))
        return -1
