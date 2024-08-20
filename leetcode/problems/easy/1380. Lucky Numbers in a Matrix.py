from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        maxs = dict()
        mins = dict()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                el = matrix[i][j]

                if i in mins:
                    if el < matrix[i][mins[i]]:
                        mins[i] = j
                else:
                    mins[i] = j

                if j in maxs:
                    if el > matrix[maxs[j]][j]:
                        maxs[j] = i
                else:
                    maxs[j] = i

        result = []
        for key in maxs:
            val = maxs[key]
            if val in mins and key == mins[val]:
                result.append(matrix[val][key])
        return result


sol = Solution()
print(sol.luckyNumbers(matrix=[
    [1, 10, 4, 2],
    [9, 3, 8, 7],
    [15, 16, 17, 12]
]))

# 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
