from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        res = 0
        m = -1
        for i in range(len(grid)):
            s = sum(grid[i])
            if s > m:
                m = s
                res = i
        return res