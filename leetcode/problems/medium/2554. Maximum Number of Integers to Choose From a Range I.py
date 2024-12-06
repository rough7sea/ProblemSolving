from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        res = 0
        sum = 0
        banned = set(banned)
        for i in range(1, n + 1):
            if sum + i > maxSum:
                return res
            if i not in banned:
                res += 1
                sum += i
        return res

sol = Solution()
print(sol.maxCount(banned = [1,6,5], n = 5, maxSum = 6))
print(sol.maxCount(banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1))
print(sol.maxCount(banned = [11], n = 7, maxSum = 50))
