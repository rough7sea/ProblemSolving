from heapq import heappush, heappop
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        queue = []

        for i in range(len(nums)):
            heappush(queue, (nums[i], i))
            if len(queue) > k:
                heappop(queue)

        while k > 0:
            num, i = heappop(queue)
            nums[i] *= multiplier
            heappush(queue, (nums[i], i))
            k -= 1

        return nums


sol = Solution()
print(sol.getFinalState(nums=[2, 1, 3, 5, 6], k=5, multiplier=2))
