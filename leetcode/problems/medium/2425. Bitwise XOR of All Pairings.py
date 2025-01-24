from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        x = 0
        if len(nums1) % 2 == 1:
            for j in nums2:
                x^=j

        if len(nums2) % 2 == 1:
            for j in nums1:
                x^=j
        return x

sol = Solution()
print(sol.xorAllNums(nums1 = [2,1,3], nums2 = [10,2,5,0]))
print(sol.xorAllNums(nums1 = [1,2], nums2 = [3,4]))