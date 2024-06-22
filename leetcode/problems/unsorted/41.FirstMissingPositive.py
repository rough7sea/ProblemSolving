from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        buckets = [0] * (len(nums) + 1)
        for n in nums:
            if n < 0 or n > len(nums):
                continue
            buckets[n] = 1

        for i in range(1, len(buckets)):
            if buckets[i] == 0:
                return i
        return len(buckets)


sol = Solution()
print(sol.firstMissingPositive([1, 2, 0]))
# print(sol.firstMissingPositive([3, 4, -1, 1]))
# print(sol.firstMissingPositive([7, 8, 9, 11, 12]))
print(sol.firstMissingPositive([1]))
print(sol.firstMissingPositive([1, 2, 3]))
