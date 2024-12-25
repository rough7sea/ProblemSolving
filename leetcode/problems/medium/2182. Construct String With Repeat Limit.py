class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:

        chars = [0] * 26
        for char in s:
            chars[ord(char) - 97] += 1

        cur = len(chars) - 1
        while cur > -1 and chars[cur] == 0:
            cur -= 1
            if cur == -1:
                return ''

        next = cur - 1
        res = ''

        while cur > -1:

            while next > -1 and chars[next] == 0:
                next -= 1

            chr_current = chr(cur + 97)

            if next > -1:
                if chars[cur] <= repeatLimit:
                    res += (chr_current * chars[cur])
                    cur = next
                    next -= 1
                    continue

                full = chars[cur] // repeatLimit
                diff = chars[cur] % repeatLimit

                extra = 1 if diff > 0 else 0

                chr_next = chr(next + 97)
                if chars[next] >= full - 1 + extra:
                    res += (
                            chr_current * repeatLimit +
                            (chr_next + chr_current * repeatLimit) * (full - 1))
                    if extra:
                        res += chr_next + chr_current * diff
                    chars[next] -= full - 1 + extra

                    cur = next
                    next -= 1
                else:
                    res += ((chr_current * repeatLimit + chr_next) * chars[next])
                    chars[cur] -= (chars[next] * repeatLimit)
                    chars[next] = 0

            else:
                res += (chr_current * min(chars[cur], repeatLimit))
                cur = next
                continue

        return res


sol = Solution()
print(sol.repeatLimitedString(s="cczazcc", repeatLimit=3))
print(sol.repeatLimitedString(s="aababab", repeatLimit=2))


