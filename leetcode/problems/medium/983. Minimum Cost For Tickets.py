from heapq import heappop, heappush
from typing import List


class Solution:
    # def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    #     costs_map = {costs[0]: 0, costs[1]: 6, costs[2]: 29}
    #     heap = [(0, 0)]
    #
    #     for i in range(len(days)):
    #
    #         while heap[0][0] < days[i]:
    #             reach, cost = heappop(heap)
    #
    #             for c in costs_map.keys():
    #                 heappush(heap, (days[i] + costs_map[c], cost + c))
    #
    #     res = heap[0][1]
    #     for _, cost in heap:
    #         res = min(res, cost)
    #
    #     return res

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last = days[-1]
        dp = [-1] * (last + 1)

        isTravelNeeded = set(days)

        def solve(dp, days, costs, currDay):
            if currDay > days[-1]:
                return 0

            if currDay not in isTravelNeeded:
                return solve(dp, days, costs, currDay + 1)

            if dp[currDay] != -1:
                return dp[currDay]

            oneDay = costs[0] + solve(dp, days, costs, currDay + 1)
            sevenDay = costs[1] + solve(dp, days, costs, currDay + 7)
            thirtyDay = costs[2] + solve(dp, days, costs, currDay + 30)

            dp[currDay] = min(oneDay, sevenDay, thirtyDay)

            return dp[currDay]

        return solve(dp, days, costs, 1)


sol = Solution()
print(sol.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))
print(sol.mincostTickets(days=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs=[2, 7, 15]))
