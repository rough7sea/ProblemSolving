from heapq import heappop, heappush
from typing import List
import copy


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        goal = str([[1, 2, 3], [4, 5, 0]])

        if str(board) == goal:
            return 0

        visited = []
        toDiscover = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    toDiscover.append((board, i, j, 0))
                    break

        while toDiscover:
            unvisited, i, j, time = heappop(toDiscover)
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (
                        0 <= i + di < len(board)
                        and 0 <= j + dj < len(board[0])
                ):

                    duplicate = copy.deepcopy(unvisited)

                    # print('before = ' + str(duplicate))
                    duplicate[i][j] = duplicate[i + di][j + dj]
                    duplicate[i + di][j + dj] = 0
                    # print('after = ' + str(duplicate) + '\n')

                    strCopy = str(duplicate)
                    if strCopy == goal:
                        return time + 1

                    if strCopy not in visited:
                        visited.append(strCopy)
                        heappush(toDiscover, (duplicate, i + di, j + dj, time + 1))

        return -1


sol = Solution()
print(sol.slidingPuzzle(
    [
        [4, 1, 2],
        [5, 0, 3]
    ]
))

# [
# [4,1,2],
# [5,0,3]
# ]
#
# [
# [4,1,2],
# [0,5,3]
# ]
#
# [
# [0,1,2],
# [4,5,3]
# ]

# [
# [1,0,2],
# [4,5,3]
# ]

# [
# [1,2,0],
# [4,5,3]
# ]

# [
# [1,2,3],
# [4,5,0]
# ]

# [
# [4,1,2],
# [5,3,0]
# ]

# [1,5,2],
# [4,0,3]
