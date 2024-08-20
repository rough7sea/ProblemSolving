from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = m - 1, n - 1
        p = len(nums1) - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1

sol = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
sol.merge(nums1, m=3, nums2=[2, 5, 6], n=3)
print(nums1)
