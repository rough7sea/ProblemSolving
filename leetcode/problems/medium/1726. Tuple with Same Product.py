from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res = 0
        cache = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                m = nums[i] * nums[j]
                cache[m] += 2

        for val in cache.values():
            if val > 3:
                res += val*(val-2)

        return res


sol = Solution()
print(sol.tupleSameProduct(nums=[2, 3, 4, 6]))
print(sol.tupleSameProduct(nums=[2, 3, 4, 6, 8, 12]))
