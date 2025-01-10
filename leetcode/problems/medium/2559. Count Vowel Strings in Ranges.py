from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}

        pref_sum = [0] * len(words)
        pref_sum[0] = 1 if words[0][0] in vowels and words[0][-1] in vowels else 0
        for i in range(1, len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                pref_sum[i] = pref_sum[i - 1] + 1
            else:
                pref_sum[i] = pref_sum[i - 1]

        res = []
        for start, end in queries:
            if start > 0:
                res.append(pref_sum[end] - pref_sum[start - 1])
            else:
                res.append(pref_sum[end])

        return res


sol = Solution()
print(sol.vowelStrings(words=["aba", "bcb", "ece", "aa", "e"], queries=[[0, 2], [1, 4], [1, 1]]))
