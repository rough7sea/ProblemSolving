from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        sorted_x = sorted(c.values(), reverse=True)
        count = 0
        circle = 1
        num = 8
        for v in sorted_x:
            count += (v * circle)
            num -= 1
            if num == 0:
                num = 8
                circle += 1

        return count


sol = Solution()
print(sol.minimumPushes('aabbccddeeffgghhiiiiii'))

