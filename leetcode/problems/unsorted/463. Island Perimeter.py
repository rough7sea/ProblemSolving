from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        r_len = len(grid)
        c_len = len(grid[0])
        for i in range(r_len):
            for j in range(c_len):
                if grid[i][j] == 0:
                    continue
                if i == 0:
                    perimeter += 1
                else:
                    if grid[i - 1][j] == 0:
                        perimeter += 1

                if j == 0:
                    perimeter += 1
                else:
                    if grid[i][j - 1] == 0:
                        perimeter += 1

                if i == r_len - 1:
                    perimeter += 1
                else:
                    if grid[i + 1][j] == 0:
                        perimeter += 1

                if j == c_len - 1:
                    perimeter += 1
                else:
                    if grid[i][j + 1] == 0:
                        perimeter += 1
        return perimeter


sol = Solution()
print(sol.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
