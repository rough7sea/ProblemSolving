from typing import List


def check_columns(cols) -> bool:
    for i in range(len(cols)):
        if cols[i] != 15:
            return False
    return True


def check_magic(i, j, grid) -> int:
    check = [0] * 15
    cols = [0] * 3
    limited = True

    for x in range(3):
        for y in range(3):
            cell = grid[i - x][j - y]
            cols[y] += cell
            check[cell - 1] = 1
            if cell > 9 or cell < 1:
                limited = False

    if limited and check_columns(cols) and check_unique(check) and check_dig(grid, i, j):
        return 1

    return 0


def check_unique(check) -> bool:
    check_sum = 0
    for x in range(len(check)):
        if check[x] == 1:
            check_sum += 1
    return check_sum == 9


def check_dig(grid, i, j) -> bool:
    dig_l = 0
    for k in range(3):
        dig_l += grid[i - k][j - k]
    return dig_l == 15


class Solution:

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 and len(grid[0]) < 3:
            return 0
        count = 0

        sum_grid = [[0] * len(grid[0]) for i in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cell = grid[i][j]
                prev = 0
                out_cell = 0
                if j > 0:
                    prev = sum_grid[i][j - 1]
                if j - 3 >= 0:
                    out_cell = grid[i][j - 3]
                sum_grid[i][j] = prev + cell - out_cell

        for i in range(2, len(grid)):
            for j in range(2, len(grid[0])):
                if sum_grid[i][j] == 15:
                    if sum_grid[i - 1][j] == 15 and sum_grid[i - 2][j] == 15:
                        count += check_magic(i, j, grid)

        return count


sol = Solution()
# print(sol.numMagicSquaresInside(
#     grid=[
#         [4, 3, 8, 4],
#         [9, 5, 1, 9],
#         [2, 7, 6, 2]
#     ]
# ))
print(sol.numMagicSquaresInside(
    grid=[
        [2, 7, 6],
        [1, 5, 9],
        [4, 3, 8]
    ]
))
# print(sol.numMagicSquaresInside(
#     grid=[
#         [3, 10, 2, 3, 4],
#         [4, 5, 6, 8, 1],
#         [8, 8, 1, 6, 8],
#         [1, 3, 5, 7, 1],
#         [9, 4, 9, 2, 9]
#     ]
# ))
# print(sol.numMagicSquaresInside(
#     grid=[
#         [9, 0, 8, 1, 6],
#         [2, 4, 3, 5, 7],
#         [4, 3, 4, 9, 2],
#         [2, 4, 5, 6, 1],
#         [9, 8, 0, 7, 8]
#     ]
# ))
# print(sol.numMagicSquaresInside(
#     grid=[
#         [8, 1, 6],
#         [3, 5, 7],
#         [4, 9, 2]
#     ]
# ))

# 4, 3, 8 - 15
# 9, 5, 1 - 15
# 2, 7, 6 - 15

# 15 15 15
# dig = 15
