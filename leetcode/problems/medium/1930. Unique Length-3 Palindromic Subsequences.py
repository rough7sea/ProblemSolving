from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        c = Counter(s)
        visited = set()
        res = 0
        for i in range(len(s)):
            if s[i] in visited:
                c[s[i]] -= 1
                if c[s[i]] == 0:
                    del c[s[i]]
                continue

            visited.add(s[i])
            if c[s[i]] < 2 or (c[s[i]] == 2 and i < len(s)-1 and s[i] == s[i+1]):
                c[s[i]] -= 1
                if c[s[i]] == 0:
                    del c[s[i]]
                continue

            t = c.copy()
            for j in range(len(s)-1, -1, -1):
                if s[j] == s[i]:
                    res += len(t.keys())
                    if c[s[i]] <= 2:
                        res -= 1
                    break

                t[s[j]] -= 1
                if t[s[j]] == 0:
                    del t[s[j]]
            c[s[i]] -= 1
            # print(s[i])
            # print(res)

        return res


sol = Solution()
print(sol.countPalindromicSubsequence("bbcbaba"))
