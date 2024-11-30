class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.rstrip().split(' ')[-1])
        count = 0
        for i in reversed(range(len(s))):
            if s[i] == ' ':
                continue
            while s[i] != ' ':
                i -= 1
                count += 1
            return count




sol = Solution()
print(sol.lengthOfLastWord('Hello    wored   '))
