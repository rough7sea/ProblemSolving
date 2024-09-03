from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left != right:
            res = max(res, min(height[left], height[right]) * (right - left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return res


sol = Solution()
print(sol.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
