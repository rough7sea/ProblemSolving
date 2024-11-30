from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        i, j = self.findRock(board)

        res = 0
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            next_i = i
            next_j = j
            while 0 <= next_i + di < len(board) and 0 <= next_j + dj < len(board[0]):
                next_i += di
                next_j += dj
                if board[next_i][next_j] == 'B':
                    break
                if board[next_i][next_j] == 'p':
                    res += 1
                    break

        return res

    def findRock(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    return i, j