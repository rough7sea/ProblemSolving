from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        peaks = [[-1 for _ in range(n)] for _ in range(m)]

        queue = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    peaks[i][j] = 0
                    queue.append((i, j))

        steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
        while queue:
            i, j = queue.popleft()
            for di, dj in steps:
                if (
                        0 <= i + di < m and
                        0 <= j + dj < n and
                        peaks[i + di][j + dj] == -1
                ):
                    peaks[i + di][j + dj] = peaks[i][j] + 1
                    queue.append((i + di, j + dj))
        return peaks


sol = Solution()
print(sol.highestPeak(isWater=[[0, 1], [0, 0]]))
print(sol.highestPeak(isWater=[[0, 0, 1], [1, 0, 0], [0, 0, 0]]))
