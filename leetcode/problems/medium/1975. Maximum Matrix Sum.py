from math import inf
from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0
        negativeCount = 0
        minValue = inf

        for i in matrix:
            for j in i:
                if j < 0:
                    negativeCount += 1
                    j = -j
                res += j
                if j < minValue:
                    minValue = j

        if negativeCount % 2 == 1:
            res -= (minValue * 2)

        return res


#  2 3 0 2 -3
# -2 3 0 2  3

# -9 8 7 6 9
#  5 4 3 2 1

# 9 8 7 6 9
#  5 4 3 2 -1


