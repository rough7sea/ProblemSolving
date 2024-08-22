from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        matrix = [[0 for i in range(n)] for j in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        if obstacleGrid[0][0] != 1:
            matrix[0][0] = 1

        for i in range(m):
            for j in range(n):

                if obstacleGrid[i][j] == 1 or i == 0 and j == 0:
                    continue

                steps = 0
                if i > 0:
                    steps += matrix[i - 1][j]
                if j > 0:
                    steps += matrix[i][j - 1]
                # if steps == 0:
                #     steps = 1
                matrix[i][j] = steps

        return matrix[m - 1][n - 1]


sol = Solution()
print(sol.uniquePathsWithObstacles(obstacleGrid=[[1, 0]]))
print(sol.uniquePathsWithObstacles(obstacleGrid=[[0, 1], [1, 0]]))
