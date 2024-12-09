from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el = None
        count = 0
        for e in nums:
            if not el:
                el = e
            if e == el:
                count += 1
            else:
                count -= 1
                if count <= 0:
                    el = e
                    count = 1
        return el


sol = Solution()
print(sol.majorityElement(nums=[1, 3, 1, 1, 4, 1, 1, 5, 1, 1, 6, 2, 2]))
