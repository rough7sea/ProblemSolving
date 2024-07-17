from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            if target == nums[l]:
                return l
            if target == nums[r]:
                return r

            m = (l + r) // 2

            if m > len(nums) - 1:
                if target < nums[r]:
                    return r
                else:
                    return r + 1
            if target == nums[m]:
                return m
            if target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return l


sol = Solution()
# print(sol.searchInsert(nums=[1, 3, 5, 6], target=5))
# print(sol.searchInsert(nums=[1, 3, 5, 6], target=2))
# print(sol.searchInsert(nums=[1, 3, 5, 6], target=7))
# print(sol.searchInsert(nums=[1, 3, 5], target=4))
# print(sol.searchInsert(nums=[1, 3, 5], target=6))
print(sol.searchInsert(nums=[3, 5, 7, 9, 10], target=8))
