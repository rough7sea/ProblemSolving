class Solution:

    def nextInt(self, c: str):
        if c == 'z':
            return ord('a')
        return ord(c) + 1

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        j = 0
        while i < len(str1) and len(str2) - j <= len(str1) - i:
            int1 = ord(str1[i])
            int2 = ord(str2[j])
            if int1 == int2 or self.nextInt(str1[i]) == int2:
                j += 1
                if j == len(str2):
                    return True
            i += 1

        return False


sol = Solution()
# print(sol.canMakeSubsequence(str1="abc", str2="ad"))
print(sol.canMakeSubsequence(str1="ab", str2="d"))
