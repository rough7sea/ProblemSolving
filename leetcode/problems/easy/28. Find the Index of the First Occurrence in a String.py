class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


sol = Solution()
print(sol.strStr(haystack="sabutsad", needle="sad"))
