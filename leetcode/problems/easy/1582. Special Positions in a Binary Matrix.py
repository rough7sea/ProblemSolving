from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [-1] * len(mat)
        cols = [-1] * len(mat[0])

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    if rows[i] == -1:
                        rows[i] = j
                    else:
                        rows[i] = -2

                    if cols[j] == -1:
                        cols[j] = i
                    else:
                        cols[j] = -2
        res = 0
        for r in rows:
            if r < 0:
                continue
            if cols[r] >= 0:
                res += 1
        return res


