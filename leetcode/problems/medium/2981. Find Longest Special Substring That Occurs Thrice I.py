from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        seqMap = defaultdict(int)
        l, r = 0, 0
        maxVal = -1
        while l < len(s):
            if r != len(s) and s[l] == s[r]:
                r += 1
                continue

            # l != r
            diff = r - l

            for n in range(diff):
                seq = (s[l], n + 1)
                seqMap[seq] += (diff - n)

                if seqMap[seq] > 2:
                    maxVal = max(maxVal, n + 1)
            l = r

        return maxVal


sol = Solution()
print(sol.maximumLength("accccbcaccccbbbbcccca"))
