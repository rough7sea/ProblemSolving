from collections import deque
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = [[False for i in range(m)] for j in range(n)]
        visited[0][0] = True
        queue = deque([(0, 0, 0)])

        while queue:
            removed, i, j = queue.popleft()
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_i = i + di
                next_j = j + dj
                if (
                        0 <= next_i < n
                        and 0 <= next_j < m
                        and not visited[next_i][next_j]
                ):
                    if next_i == n - 1 and next_j == m - 1:
                        return removed
                    visited[next_i][next_j] = True
                    if grid[next_i][next_j] == 1:
                        queue.append((removed + 1, next_i, next_j))
                    else:
                        queue.appendleft((removed, next_i, next_j))
        return -1


sol = Solution()
# print(sol.minimumObstacles(grid=[[0, 1, 1], [1, 1, 0], [1, 1, 0]]))
print(sol.minimumObstacles(grid=[[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]))
print(sol.minimumObstacles(grid=[
    [0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 1, 0]
]))
