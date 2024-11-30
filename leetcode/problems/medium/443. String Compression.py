from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        prev = None
        times = 0
        for e in chars:
            if prev is None:
                prev = e
                times = 1
                continue
            if e == prev:
                times += 1
                continue

            chars[idx] = prev
            idx += 1
            if times > 1:
                for t in str(times):
                    chars[idx] = t
                    idx += 1

            prev = e
            times = 1

        chars[idx] = prev
        idx += 1
        if times > 1:
            for t in str(times):
                chars[idx] = t
                idx += 1
        return idx


sol = Solution()
print(sol.compress(chars=["a", "a", "b", "b", "c", "c", "c"]))
print(sol.compress(chars=["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
