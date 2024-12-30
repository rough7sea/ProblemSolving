from collections import defaultdict
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        M = 1000000007
        freq_map = defaultdict(int)
        window_size = len(words[0]) - len(target) + 1

        for i in range(len(target)):
            prev_t = target[i]
            for i_d in range(0, window_size):
                if (i + i_d, prev_t) in freq_map:
                    continue

                for word in words:
                    if word[i + i_d] == prev_t:
                        freq_map[(i + i_d, prev_t)] += 1

        dp = dict()
        prev_row_sum = 1

        for i in range(0, len(target)):
            prev_t = target[i - 1]
            t = target[i]
            new_row_sum = 0
            for i_d in range(window_size - 1, -1, -1):
                dp_t_i = i + i_d
                dp[(dp_t_i, t)] = (prev_row_sum * freq_map[(dp_t_i, t)]) % M
                if i > 0:
                    prev_row_sum -= dp[(dp_t_i - 1, prev_t)]
                new_row_sum += dp[(dp_t_i, t)]
            prev_row_sum = new_row_sum

        res = 0
        t = target[-1]
        for i in range(window_size):
            res = (res + dp[(len(words[0]) - 1 - i, t)]) % M

        return res


sol = Solution()
print(sol.numWays(words=["acca", "bbbb", "caca"], target="aba"))  # 6
print(sol.numWays(words=["abba", "baab"], target="bab"))  # 4
