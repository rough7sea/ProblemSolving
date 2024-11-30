from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        maxDiff = 0
        prevMin = prices[0]
        for stock in prices:
            prevMin = min(prevMin, stock)
            maxDiff = max(maxDiff, stock - prevMin)
        return maxDiff