from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        if n == 1:
            return 0

        pref_sum = [0 for _ in range(n)]
        suf_sum = [0 for _ in range(n)]

        pref_sum[-1] = grid[0][-1]
        suf_sum[0] = grid[1][0]

        for i in range(1, n-1):
            pref_sum[n-i-1] += pref_sum[n-i] + grid[0][n-i-1]
            suf_sum[i] += suf_sum[i-1] + grid[1][i]

        for i in range(n-1):
            if pref_sum[i+1] <= suf_sum[i]:
                if i > 0:
                    return max(pref_sum[i+1], suf_sum[i-1])
                return pref_sum[i+1]

        return suf_sum[-2]

sol = Solution()
# print(sol.gridGame(grid = [[1,3,1,15],[1,3,3,1]]))
# print(sol.gridGame(grid = [[2,5,4],[1,5,1]]))
# print(sol.gridGame(grid = [
#     [20,3,20,17,2,12,15,17,4,15],
#     [20,10,13,14,15,5,2,3,14,3]
# ]))
print(sol.gridGame(grid = [[10,12,14,19,19,12,19,2,17],[20,7,17,14,3,1,1,17,12]]))