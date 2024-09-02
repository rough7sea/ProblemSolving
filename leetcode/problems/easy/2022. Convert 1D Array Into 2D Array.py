from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        res = []
        for i in range(m):
            res.append(original[i * n:i * n + n])
        return res


sol = Solution()
print(sol.construct2DArray(original = [1,2,3,4], m = 2, n = 2))
