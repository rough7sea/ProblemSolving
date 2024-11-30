from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        arr1.sort()

        res = 0
        i, j = 0, 0
        lastCompr = None
        while i < len(arr1) and j < len(arr2):
            if abs(arr1[i] - arr2[j]) > d:
                if arr1[i] < arr2[j]:
                    if lastCompr != i:
                        res += 1
                    i += 1
                else:
                    j += 1
            else:
                lastCompr = i
                i += 1

        res += len(arr1) - i

        return res


sol = Solution()
# print(sol.findTheDistanceValue(arr1=[1, 4, 2, 3], arr2=[-4, -3, 6, 10, 20, 30], d=3))
print(sol.findTheDistanceValue(arr1=[2, 1, 100, 3], arr2=[-5, -2, 10, -3, 7], d=6))

# 1 2 4 5 5 6
# 3 3 3 3 4 5 6
