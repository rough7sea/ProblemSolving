from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 1
        k = len(nums)
        for i in reversed(range(len(nums) - 1)):
            if nums[i] == nums[i + 1]:
                del nums[i]
                k -= 1
        return k


sol = Solution()
nums = [1, 1, 2]
# print()
sol.removeDuplicates(nums)
print(nums)
