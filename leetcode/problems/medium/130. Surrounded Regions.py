from typing import List


steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = [[0 for i in range(len(board[0]))] for j in range(len(board))]

        def journeyNotSurrounded(x, y):
            visited[x][y] = 1
            for dx, dy in steps:
                if (0 <= dx + x < len(board) and
                        0 <= dy + y < len(board[x]) and
                        board[x + dx][y + dy] == "O" and
                        visited[x + dx][y + dy] == 0):
                    journeyNotSurrounded(x + dx, y + dy)

        for i in range(len(board)):
            if i == 0 or i == len(board) - 1:
                r = range(len(board[0]))
            else:
                r = [0, len(board[0]) - 1]
            for j in r:
                if board[i][j] == "O" and visited[i][j] == 0:
                    journeyNotSurrounded(i, j)
                visited[i][j] = 1

        for i in range(len(board)):
            for j in range(len(board[0])):
                if visited[i][j] == 0:
                    board[i][j] = "X"



sol = Solution()


# board = [
#     ["X","X","X","X"],
#     ["X","O","O","X"],
#     ["X","X","O","X"],
#     ["X","O","X","X"]
# ]

# board = [
#     ["X","X","X","X"],
#     ["X","O","O","X"],
#     ["X","O","O","X"],
#     ["X","X","X","O"]
# ]
#
# board =[
#     ["X","O","X"],
#     ["O","X","O"],
#     ["X","O","X"]
# ]
board =[
    ["O","X","X","O","X"],
    ["X","O","O","X","O"],
    ["X","O","X","O","X"],
    ["O","X","O","O","O"],
    ["X","X","O","X","O"]
]

sol.solve(board)
print(board)

