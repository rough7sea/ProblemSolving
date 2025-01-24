from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        visited = [[-1 for j in range(n)] for i in range(m)]

        steps = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(i, j, island) -> bool:
            visited[i][j] = island
            if 0 == i or 0 == j or i == m-1 or j == n-1:
                return False
            res = True
            for di, dj in steps:
                if (
                        0 <= i + di < m and
                        0 <= j + dj < n and
                        heightMap[i][j] <= heightMap[i + di][j + dj] and
                        visited[i + di][j + dj] == -1
                ):
                    res &= dfs(i + di, j + dj, island)
            return res

        water = set()

        islands = 1

        for i in (0, m-1):
            for j in range(n):
                if visited[i][j] == -1:
                    dfs(i, j, 0)



        for i in range(m):
            for j in (0, n-1):
                if visited[i][j] == -1:
                    dfs(i, j, 0)

        # for i in range(m):
        #     for j in range(n):
        #         if visited[i][j] == -1:
        #             if dfs(i, j, islands):
        #                 water.add(islands)
        #             islands += 1

        return 0


sol = Solution()
print(sol.trapRainWater(heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))