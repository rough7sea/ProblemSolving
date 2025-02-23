class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = []
        if pattern[0] == 'I':
            res.append(1)
            cur = 2
        else:
            cur = 1
        d = 0
        for i in range(len(pattern)):
            if pattern[i] == 'D':
                d += 1
                continue

            if d > 0:
                for j in range(d + 1):
                    res.append(cur + d - j)
                cur += d + 1
                d = 0

            if i == len(pattern) - 1 or pattern[i + 1] == 'I':
                res.append(cur)
                cur += 1

        if d > 0:
            for j in range(d + 1):
                res.append(cur + d - j)

        return ''.join([str(x) for x in res])


sol = Solution()
print(sol.smallestNumber('IIIDIDDD'))
# 123549876
print(sol.smallestNumber('DDD'))
# 4321
print(sol.smallestNumber('IIIDDD'))
