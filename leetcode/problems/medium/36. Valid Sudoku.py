from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        area = [[[] for _ in range(3)] for _ in range(3)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                e = board[i][j]
                if e == ".":
                    continue
                rows[i].append(e)
                cols[j].append(e)

                if i < 3:
                    a = area[0]
                elif i < 6:
                    a = area[1]
                else:
                    a = area[2]

                if j < 3:
                    a = a[0]
                elif j < 6:
                    a = a[1]
                else:
                    a = a[2]
                a.append(e)

        for l in rows:
            if len(set(l)) != len(l):
                return False

        for c in cols:
            if len(set(c)) != len(c):
                return False

        for r in area:
            for a in r:
                if len(set(a)) != len(a):
                    return False
        return True


sol = Solution()
print(sol.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                         [".", "9", "8", ".", ".", ".", ".", "6", "."],
                         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                         [".", "6", ".", ".", ".", ".", "2", "8", "."],
                         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
