from typing import List


def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2] if n else None


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        return median(nums1)


sol = Solution()
print(sol.findMedianSortedArrays([1, 2, 3], [4, 5, 6, 7]))
