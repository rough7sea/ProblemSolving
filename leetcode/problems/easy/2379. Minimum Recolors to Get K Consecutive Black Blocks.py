from collections import defaultdict


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window = defaultdict(int)
        res = len(blocks)
        left = 0

        for i, block in enumerate(blocks):
            window[block] += 1
            if i >= k - 1:
                res = min(res, window['W'])
                if res == 0:
                    return res
                window[blocks[left]] -= 1
                left += 1

        return res

sol = Solution()
print(sol.minimumRecolors(blocks = "WBBWWBBWBW", k = 7))
print(sol.minimumRecolors(blocks = "WBWBBBW", k = 2))
print(sol.minimumRecolors(blocks = "BWWWBB", k = 6))
print(sol.minimumRecolors(blocks = "BBBBBWWBBWBWBWWWBWBWBBBBWBBBBWBWBWBWBWWBWWBWBWWWWBBWWWWBWWWWBWBBWBBWBBWWW", k = 29))
