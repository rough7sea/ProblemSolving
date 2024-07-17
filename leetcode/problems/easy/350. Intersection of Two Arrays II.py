from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < 1 or len(nums1) < 1:
            return []
        nums1.sort()
        nums2.sort()
        i, j = [0, 0]
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1

        return result


    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     dct = Counter(nums1)
    #     result = []
    #
    #     for n2 in nums2:
    #         if n2 in dct and dct[n2]>0:
    #             result.append(n2)
    #             dct[n2] -= 1
    #
    #     return result


sol = Solution()
print(sol.intersect([3, 2, 3], [1, 3, 3]))
print(sol.intersect([1, 2], [1, 1]))
print(sol.intersect([7, 2, 2, 4, 7, 0, 3, 4, 5], [3, 9, 8, 6, 1, 9]))
