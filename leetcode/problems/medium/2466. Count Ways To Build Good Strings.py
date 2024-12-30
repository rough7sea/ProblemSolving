from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    # def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
    #     m = 10 ** 9 + 7
    #
    #     dp = defaultdict(int)
    #     visited = set()
    #     heap = [0]
    #     dp[0] = 1
    #
    #     res = 0
    #     while heap:
    #         next = heappop(heap)
    #         if next >= high:
    #             break
    #         for el in (zero, one):
    #             dp[next + el] = (dp[next + el] + dp[next]) % m
    #             if low <= next + el <= high:
    #                 res = (res + dp[next]) % m
    #             if next + el not in visited:
    #                 heappush(heap, next + el)
    #                 visited.add(next + el)
    #
    #     return res

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        m = 10 ** 9 + 7
        dp = [0] * (high + 1)
        heap = [0]
        dp[0] = 1

        res = 0
        while heap:
            next = heappop(heap)
            if next >= high:
                break

            for el in (zero, one):
                if next + el > high:
                    continue
                if dp[next + el] == 0:
                    heappush(heap, next + el)

                dp[next + el] = (dp[next + el] + dp[next]) % m
                if low <= next + el <= high:
                    res = (res + dp[next]) % m
        return res


sol = Solution()
print(sol.countGoodStrings(low=3, high=3, zero=1, one=1))
print(sol.countGoodStrings(low=2, high=3, zero=1, one=2))

# 0

# 0 0
# 11

# 0 0 0
# 0 11
# 11 0


# zero = 3, one = 5

# diff = 2
# sum = 8


# 000
# 11111

# 000 000

# 000 11111
# 11111 000


# 3,  5,     6,   8,        9,   10,    11,    12,   13,    14,     15

# [1], [1], [1], [1 + 1],  [1], [1], [1 + 2], [1],  [2 + 1], [1 + 3], [1]

# 1, 1, 2

# [2], [2 + 2]

# 0 00 01
# 1 10 11
