from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' and (i - 1 < 0 or board[i - 1][j] != 'X') and (
                        j - 1 < 0 or board[i][j - 1] != 'X'):
                    count += 1
        return count


sol = Solution()
print(sol.countBattleships(board=[
    ["X", ".", ".", "X"],
    [".", ".", ".", "X"],
    [".", ".", ".", "X"]
]))

print(sol.countBattleships(board=[
    ["X"],
]))
