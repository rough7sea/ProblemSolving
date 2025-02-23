from collections import defaultdict
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        res = int(n * (n - 1) / 2)
        map = defaultdict(int)
        for i in range(n):
            map[nums[i] - i] += 1
        for val in map.values():
            if val > 1:
                res -= (val * (val - 1) / 2)
        return res
