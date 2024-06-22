from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count


sol = Solution()
print(sol.heightChecker([1, 1, 4, 2, 1, 3]))
print(sol.heightChecker([1, 1, 4, 2, 1, 3, 2, 4]))
# [1, 1, 4, 2, 1, 3, 2, 4]
# [1, 1, 1, 2, 2, 3, 4, 4]
print(sol.heightChecker([1, 2, 3, 4, 5]))
print(sol.heightChecker([5, 1, 2, 3, 4]))
