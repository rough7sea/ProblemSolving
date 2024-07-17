class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = numBottles
        rest = numBottles
        while rest >= numExchange:
            drink += (rest // numExchange)
            rest = (rest // numExchange) + (rest % numExchange)
        return drink


sol = Solution()
print(sol.numWaterBottles(numBottles=15, numExchange=4))


# 15 / 4 = 3

# 15 % 4 = 3

# 15 + 3 + 1 = 19.
