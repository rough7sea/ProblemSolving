from heapq import heapify, heappushpop
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = nums[:min(k, len(nums))]
        heapify(pq)
        for i in range(k, len(nums)):
            heappushpop(pq, nums[i])
        return pq[0]

    # def findKthLargest(self, nums, k):
    #     min_value = min(nums)
    #     max_value = max(nums)
    #     count = [0] * (max_value - min_value + 1)
    #
    #     for num in nums:
    #         count[num - min_value] += 1
    #
    #     remain = k
    #     for num in range(len(count) - 1, -1, -1):
    #         remain -= count[num]
    #         if remain <= 0:
    #             return num + min_value
    #
    #     return -1


sol = Solution()
print(sol.findKthLargest(nums=[3, 4, 1, 5, 6, 4], k=2))
