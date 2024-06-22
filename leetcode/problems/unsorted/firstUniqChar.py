class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = {}
        repeated = set()

        for i in range(len(s)):
            char = s[i]
            if char in repeated:
                continue
            if char in unique:
                unique.pop(char)
                repeated.add(char)
            else:
                unique[char] = i

        if len(unique) > 0:
            return unique[list(unique.keys())[0]]
        return -1


sol = Solution()
print(sol.firstUniqChar('loveleetcode'))
print(sol.firstUniqChar('aabb'))
