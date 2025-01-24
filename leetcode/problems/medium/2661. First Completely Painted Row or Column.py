from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        map = [(0, 0) for _ in range(n * m + 1)]

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                el = mat[i][j]
                map[el] = (i, j)

        rows = [0 for _ in range(m + 1)]
        cols = [0 for _ in range(n + 1)]

        for i in range(len(arr)):
            row, col = map[arr[i]]
            rows[row] += 1
            if rows[row] == n:
                return i
            cols[col] += 1
            if cols[col] == m:
                return i

        return 0

sol = Solution()
# print(sol.firstCompleteIndex(arr = [1,3,4,2], mat = [[1,4],[2,3]]))
# print(sol.firstCompleteIndex(arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]))
# print(sol.firstCompleteIndex(arr = [1,4,5,2,6,3], mat = [[4,3,5],[1,2,6]]))
print(sol.firstCompleteIndex(arr = [8,2,4,9,3,5,7,10,1,6], mat = [[8,2,9,10,4],[1,7,6,3,5]]))

