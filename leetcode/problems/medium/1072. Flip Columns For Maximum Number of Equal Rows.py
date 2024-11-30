from collections import defaultdict, Counter
from typing import List


class Solution:
    # def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
    #     map = defaultdict(int)
    #
    #     for i in range(len(matrix)):
    #         pattern = ''
    #         prev = None
    #         prevSum = 0
    #         for j in range(len(matrix[0])):
    #             if prev is None or matrix[i][j] == prev:
    #                 prevSum += 1
    #                 prev = matrix[i][j]
    #             else:
    #                 pattern += str(prevSum)
    #                 pattern += '|'
    #                 prevSum = 1
    #                 prev = matrix[i][j]
    #         pattern += str(prevSum)
    #         map[pattern] += 1
    #     return max(map.values())
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = Counter()
        for row in matrix:
            t = tuple(row) if row[0] == 0 else tuple(x ^ 1 for x in row)
            cnt[t] += 1
        return max(cnt.values())

sol = Solution()
# print(sol.maxEqualRowsAfterFlips(matrix = [[0, 0, 0],[0, 0, 1],[1, 1, 0]]))
print(sol.maxEqualRowsAfterFlips(matrix=[[0, 1], [1, 1]]))

#  1 0 0 0 0 | 4
#  1 0 0 0 0 | 4
#  0 1 0 1 1 | 2
#  0 0 1 1 0 | 3

#  2 3 3 2 3 - 2


#  1 0 0 0 0 | 4
#  1 0 0 0 0 | 4
#  0 0 0 1 1 | 3
#  0 1 1 1 0 | 2

#  2 3 3 2 3 - 2


#  1 0 0 0 0 | 1
#  0 0 0 0 0 | 0
#  0 0 0 1 1 | 2
#  1 1 1 1 0 | 1

#  2 3 3 2 3 - 1?


#  1 0 0 0 0 | 1
#  1 1 1 1 1 | 5
#  0 0 0 1 1 | 2
#  1 1 1 1 0 | 1

#  1 2 2 1 2 - 1?

#  1 0 0 0 1 | 2
#  0 0 0 0 1 | 1
#  0 0 0 1 0 | 1
#  1 1 1 1 1 | 0

#  2 3 3 2 1 - 1

#  0 0 0 1 | 1
#  0 0 1 0 | 1
#  0 1 0 0 | 1
#  1 0 0 0 | 1

#  3 3 3 3 - 1

#  0 0 0 1 | 1
#  0 0 0 1 | 1
#  0 0 0 1 | 1
#  0 0 0 1 | 1

#  4 4 4 0 - 4

#  0 0 0 0 | 0/4
#  0 0 0 0 | 0/4
#  0 0 0 0 | 0/4
#  0 0 0 0 | 0/4

#  4 4 4 4 - 4


#  1 0 0 0 1 | 2
#  0 0 0 0 1 | 1
#  0 0 0 1 0 | 1
#  0 0 0 0 0 | 0/5

#  3 4 4 3 2 - 1


# 0 1 1 | 2
# 1 0 0 | 1
# 1 0 0 | 1

# 2 1 1 - 2


# 0 0 0 | 0/3
# 1 1 1 | 2
# 1 1 1 | 2

# 2 2 2 - 2
