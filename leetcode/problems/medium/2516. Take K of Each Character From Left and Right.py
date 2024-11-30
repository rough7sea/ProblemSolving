from collections import defaultdict


class Solution:

    def isMapFull(self, map: dict, k):
        for e in ['a', 'b', 'c']:
            if map[e] < k:
                return False

        return True

    def circleIndex(self, i, s: str):
        return i % len(s)

    def inEdges(self, left, right, s: str):
        if left > right:
            return True
        if 0 < left and right < len(s) - 1 or left >= len(s):
            return False
        return True

    # def takeCharacters(self, s: str, k: int) -> int:
    #     if k == 0:
    #         return 0
    #     if len(s) < 3:
    #         return -1
    #     map = defaultdict(int)
    #     left = 0
    #     right = 0
    #     map[s[0]] += 1
    #     res = -1
    #
    #     while left < len(s):
    #         while self.circleIndex(right + 1, s) != left:
    #             right = self.circleIndex(right + 1, s)
    #             map[s[right]] += 1
    #             if self.isMapFull(map, k):
    #                 if self.inEdges(left, right, s):
    #                     res = self.getTotal(map, res)
    #                 break
    #
    #         if not self.isMapFull(map, k):
    #             return res
    #
    #         while self.isMapFull(map, k) and self.inEdges(left, right, s) and left < len(s):
    #             res = self.getTotal(map, res)
    #             map[s[self.circleIndex(left, s)]] -= 1
    #             left += 1
    #
    #     if self.isMapFull(map, k):
    #         res = self.getTotal(map, res)
    #
    #     return res

    def getTotal(self, map, res):
        sum = map['a'] + map['b'] + map['c']
        if res == -1:
            return sum
        return min(res, sum)

    def takeCharacters(self, s: str, k: int) -> int:
        freqs = [0] * 3
        n = len(s)

        for c in s:
            freqs[ord(c) - ord('a')] += 1

        i = 0
        j = 0
        if freqs[0] < k or freqs[1] < k or freqs[2] < k:
            return -1

        for j in range(n):
            freqs[ord(s[j]) - ord('a')] -= 1

            if freqs[0] < k or freqs[1] < k or freqs[2] < k:
                freqs[ord(s[i]) - ord('a')] += 1
                i += 1


        return n - (j - i + 1)


sol = Solution()
print(sol.takeCharacters(s="abc", k=1))
print(sol.takeCharacters(s="acccc", k=4))
print(sol.takeCharacters(s="acba", k=1))
print(sol.takeCharacters(s="ccbabcc", k=1))
print(sol.takeCharacters(s="ccbcac", k=1))
print(sol.takeCharacters(s="aabaaaacaabc", k=2))



