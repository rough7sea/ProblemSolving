from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)

        while left < right:
            m = (left + right) // 2

            if matrix[m][0] == target or matrix[m][-1] == target:
                return True

            if matrix[m][0] < target < matrix[m][-1]:
                break

            if matrix[m][0] < target:
                left = m + 1
            else:
                right = m

        row = matrix[m]
        left = 0
        right = len(row)

        while left < right:
            m = (left + right) // 2

            if row[m] == target:
                return True

            if row[m] < target:
                left = m + 1
            else:
                right = m
        return False

sol = Solution()
print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
