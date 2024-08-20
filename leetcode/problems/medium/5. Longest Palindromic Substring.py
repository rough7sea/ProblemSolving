class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        for i in range(len(s)):
            res = self.method_name(i, i, res, s)
            res = self.method_name(i, i + 1, res, s)

        return res

    def method_name(self, l, r, res, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(res):
                res = s[l:r + 1]
            l -= 1
            r += 1
        return res


sol = Solution()
print(sol.longestPalindrome('abbababa'))
print(sol.longestPalindrome('babad'))
print(sol.longestPalindrome('cbbd'))
print(sol.longestPalindrome('ccc'))
print(sol.longestPalindrome('aaaa'))
