from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        left_s = 0
        for i in range(len(arr)):
            left_s += arr[i]
            total -= arr[i]
            if left_s * 2 == total:
                break
        i += 1
        if i >= len(arr):
            return False

        for j in range(i, len(arr) - 1):
            total -= arr[j]

            if total == left_s:
                return True
        return False


sol = Solution()
# print(sol.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))
print(sol.canThreePartsEqualSum([1, -1, 1, -1]))
