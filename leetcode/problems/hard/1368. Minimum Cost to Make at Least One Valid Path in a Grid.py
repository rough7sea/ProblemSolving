from collections import deque
from heapq import heappop, heappush
from typing import List


# 1 - right. (i.e go from grid[i][j] to grid[i][j + 1])
# 2 - left. (i.e go from grid[i][j] to grid[i][j - 1])
# 3 - down (i.e go from grid[i][j] to grid[i + 1][j])
# 4 - up grid[i - 1][j]

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return 0

        heap = deque([(0, 0, 0)])
        visited = [[-1 for i in range(n)] for j in range(m)]
        visited[0][0] = 0

        while heap:
            # cost, i, j = heappop(heap)
            cost, i, j = heap.popleft()

            if i == m - 1 and j == n - 1:
                return cost

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (
                        0 <= i + di < m and
                        0 <= j + dj < n
                ):
                    if (
                            (grid[i][j] == 1 and dj == 1) or
                            (grid[i][j] == 2 and dj == -1) or
                            (grid[i][j] == 3 and di == 1) or
                            (grid[i][j] == 4 and di == -1)
                    ):
                        next_cost = cost
                    else:
                        next_cost = cost + 1

                    if visited[i + di][j + dj] == -1 or next_cost < visited[i + di][j + dj]:
                        visited[i + di][j + dj] = next_cost
                        if next_cost > cost:
                            # heappush(heap, (next_cost, i + di, j + dj))
                            heap.append((next_cost, i + di, j + dj))
                        else:
                            heap.appendleft((next_cost, i + di, j + dj))

        return -1

sol = Solution()
print(sol.minCost(grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))
print(sol.minCost(grid = [[1,1,3],[3,2,2],[1,1,4]]))