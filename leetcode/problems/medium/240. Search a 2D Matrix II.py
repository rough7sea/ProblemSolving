from bisect import bisect_left
from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        if target == matrix[0][0] or target == matrix[-1][-1]:
            return True

        i = bisect_left(matrix[0], target)
        if i == -1:
            return False

        if i < len(matrix[0]) and matrix[0][i] == target:
            return True

        for j in range(i):
            left = 0
            right = len(matrix) - 1
            while left <= right:
                mid = left + (right - left) // 2
                # Check if x is present at mid
                if matrix[mid][j] == target:
                    return True
                # If x is greater, ignore left half
                elif matrix[mid][j] < target:
                    left = mid + 1
                # If x is smaller, ignore right half
                else:
                    right = mid - 1
        return False

sol = Solution()
print(sol.searchMatrix(matrix = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]], target = 5))

print(sol.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20))

print(sol.searchMatrix(matrix = [[-5]], target = -5))
print(sol.searchMatrix(matrix = [[5],[6]], target = 6))
print(sol.searchMatrix(matrix = [[1,3,5]], target = 3))



