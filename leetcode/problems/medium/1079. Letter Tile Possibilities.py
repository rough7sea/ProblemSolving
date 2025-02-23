from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        def rec(counter: Counter) -> int:
            if len(counter.keys()) == 0:
                return 1
            c = 1
            for key in counter.keys():
                counterCopy = counter.copy()
                counterCopy[key] -= 1
                if counterCopy[key] == 0:
                    del counterCopy[key]
                c += rec(counterCopy)
            return c

        return rec(Counter(tiles)) - 1


sol = Solution()
print(sol.numTilePossibilities('AAABBC'))
print(sol.numTilePossibilities('AAB'))

# AAABBC
# print(math.factorial(2) * (math.factorial(3)))
# print(math.factorial(6) / math.factorial(3))

# AAB
# print(math.factorial(3) / math.factorial(2))
