from heapq import heappush, heappop
from typing import List


class Solution:

    # brut force
    # def smallestDistancePair(self, nums: List[int], k: int) -> int:
    #     pq = []
    #     for i in range(len(nums) - 1):
    #         for j in range(i + 1, len(nums)):
    #             print(f'{nums[i]} - {nums[j]}')
    #             heappush(pq, -abs(nums[i] - nums[j]))
    #             if len(pq) > k:
    #                 heappop(pq)
    #     return abs(pq[0])

    # Use binary search on possible pair distances (from 0 to the maximum difference in the sorted array).
    # For each midpoint in the binary search, count pairs with distances ≤ this midpoint.
    # Adjust the search range based on whether the count is less than or greater than k.
    # This method efficiently narrows down to the k-th smallest distance by leveraging sorting and binary search.

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        right = max(nums)

        while left < right:
            mid = left + ((right - left) // 2)
            diffs = self.slide_and_count(nums, mid)
            if diffs >= k:
                right = mid
            else:
                left = mid + 1
        return right

    def slide_and_count(self, nums, mid) -> int:
        count = 0
        left = 0

        for right in range(len(nums)):
            while nums[right] - nums[left] > mid:
                left += 1
            count += right - left
        return count


sol = Solution()
print(sol.smallestDistancePair([1, 2, 3, 4, 5, 6, 7, 8], 4))
print(sol.smallestDistancePair([1, 2, 2, 4, 5, 6, 7], 7))
# print(sol.slide_and_count([1, 2, 3, 4, 5, 6, 7, 8], 4))

