import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> float:
        # if n == 1 or m == 1:
        #     return 1
        # if n == 2 or m == 2:
        #     if m > n:
        #         return pow((m - 2), (n - 1)) + 2
        #     else:
        #         return pow((n - 2), (m - 1)) + 2
        #
        # if n - 2 > m - 2:
        #     return pow((n - 2), (m - 1)) + 2 + 1
        # return pow((m - 2), (n - 1)) + 2 + 1
        # (m+n-2)!/((m-1)!(n-1))!
        return math.factorial((m + n - 2)) / math.factorial(math.factorial(m-1) * (n-1))



sol = Solution()
print(sol.uniquePaths(3, 3))


# (3 * 7 - m - n) * 2

# Input: m = 3, n = 2
# Output: 3

#  R []
# [] []
# [] *

#  R [] []
# [] [] []
# [] [] *

#  R []
# [] []
# [] []
# [] *


# Input: m = 3, n = 7
# Output: 28

# base (n1 + m3) + (m1 + n7) = 2
# 5 * 5 = 25

# 25 + 2 + 1 = 28 ...

#  R [] [] [] [] [] []
# [] [] [] [] [] [] []
# [] [] [] [] [] [] *

# Input: m = 7, n = 3
# Output: 28

#  R [] []
# [] [] []
# [] [] []
# [] [] []
# [] [] []
# [] [] []
# [] [] *


