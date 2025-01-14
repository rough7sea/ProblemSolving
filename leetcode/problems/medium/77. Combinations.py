from itertools import combinations
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
    #     if k == 1:
    #         return [[i] for i in range(1,n+1)]
    #     if k == n:
    #         return [[i for i in range(1, n+1)]]
    #
    #     def rec(state: list[int]) -> list[list[int]]:
    #         if len(state) == k:
    #             return [ state.copy()]
    #
    #         start = 0 if len(state) == 0 else state[-1]
    #         res = []
    #         for i in range(start + 1, n + 1):
    #             state.append(i)
    #             res += rec(state)
    #             state.pop()
    #         return res
    #
    #     return rec([])

        return list(combinations([i for i in range(1, n+1)], k))

sol = Solution()
print(sol.combine(n = 4, k = 3))
