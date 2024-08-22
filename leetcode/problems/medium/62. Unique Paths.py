class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for i in range(n)] for j in range(m)]
        matrix[0][0] = 1
        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                steps = 0
                if i > 0:
                    steps += matrix[i - 1][j]

                if j > 0:
                    steps += matrix[i][j - 1]

                if steps == 0:
                    steps = 1
                matrix[i][j] = steps

        return matrix[m - 1][n - 1]


sol = Solution()
print(sol.uniquePaths(3, 7))
print(sol.uniquePaths(1, 1))

