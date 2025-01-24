from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = [None] * len(grid)
        cols = [None] * len(grid[0])
        servers = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if rows[i]:
                        servers.add((i, j))
                        servers.add(rows[i])
                    if cols[j]:
                        servers.add((i, j))
                        servers.add(cols[j])
                    rows[i] = (i, j)
                    cols[j] = (i, j)

        return len(servers)


sol = Solution()
print(sol.countServers(grid=[[1, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0]]))
