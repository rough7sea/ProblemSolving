from collections import defaultdict
from heapq import heappop, heapify
from typing import List


class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        paint = defaultdict(int)
        for start, end, color in segments:
            paint[start] += color
            paint[end] -= color

        res = []
        intervals = sorted(list(paint.keys()))
        color = 0
        for i in range(1, len(intervals)):
            color += paint[intervals[i-1]]
            if color != 0:
                # yield ([intervals[i - 1], intervals[i], color])
                res.append([intervals[i-1], intervals[i], color])
        return res
        # return []


sol = Solution()
print(sol.splitPainting(segments=[[1, 7, 9], [6, 8, 15], [8, 10, 7]]))
# [[1,6,9],[6,7,24],[7,8,15],[8,10,7]]
# print(sol.splitPainting(segments=[[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]]))
# [[1,4,12],[4,7,12]]
print(sol.splitPainting(segments=
                        [[4, 5, 9], [8, 12, 5], [4, 7, 19], [14, 15, 1], [3, 10, 8], [17, 20, 18], [7, 19, 14],
                         [8, 16, 6], [14, 17, 7], [11, 13, 3]]))

# [[3,4,8],[4,5,36],[5,7,27],[7,8,22],[8,10,33],[10,11,25],[11,12,28],
# [12,13,23],[13,14,20],[14,15,28],[15,16,27],[16,17,21],[17,19,32],[19,20,18]]
