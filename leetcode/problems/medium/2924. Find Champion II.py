from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        map = [0 for i in range(n)]

        for edge in edges:
            e, v = edge
            map[v] = 1

        res = -1
        for i in range(n):
            if map[i] == 0:
                if res > -1:
                    return -1
                res = i

        return res


sol = Solution()
print(sol.findChampion(n=3, edges=[[0, 1], [1, 2]]))
