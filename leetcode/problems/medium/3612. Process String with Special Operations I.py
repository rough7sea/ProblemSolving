class Solution:
    def processStr(self, s: str) -> str:
        r = ''

        for ch in s:
            if ch == '#':
                r += r
                continue

            if ch == '%':
                r = r[::-1]
                continue

            if ch == '*':
                if len(r) >= 1:
                    r = r[:-1]
                continue
            r += ch
        return r

sol = Solution()
print(sol.processStr("a#b%*"))
print(sol.processStr("z*#"))