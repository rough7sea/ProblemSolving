class Solution:
    def reverse(self, x: int) -> int:
        limit = 2147483647
        s = str(x)
        if s[0] == '-':
            rev = -int(str(x)[:0:-1])
        else:
            rev = int(str(x)[::-1])

        if abs(rev) > limit:
            return 0
        return rev


sol = Solution()
print(sol.reverse(123))
print(sol.reverse(-321))
