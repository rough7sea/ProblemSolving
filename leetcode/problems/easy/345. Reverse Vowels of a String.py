
vowels = {"a", "e", "i", "o", "u"}

class Solution:
    def reverseVowels(self, s: str) -> str:

        if len(s) <= 1:
            return s

        i = 0
        j = len(s) - 1

        head, tail = "", ""

        while i < j:

            if s[i].lower() not in vowels:
                head += s[i]
                i += 1
                continue

            if s[j].lower() not in vowels:
                tail += s[j]
                j -= 1
                continue

            head += s[j]
            tail += s[i]
            j -= 1
            i += 1

        if i == j:
            return head + s[i] + tail[::-1]

        return head + tail[::-1]

sol = Solution()
print(sol.reverseVowels("IceCreAm"))
print(sol.reverseVowels("leetcode"))
print(sol.reverseVowels("ai"))
print(sol.reverseVowels("!!!"))