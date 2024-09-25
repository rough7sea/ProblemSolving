class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        for e in '{0:b}'.format(start ^ goal):
            if e == '1':
                count += 1
        return count


# 1010
# 0111

print(Solution().minBitFlips(10, 7))

# y = int(a, 2) ^ int(b, 2)
# print('{0:b}'.format(y))
