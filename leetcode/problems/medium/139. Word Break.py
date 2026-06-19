from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict.sort(key=lambda x: len(x))

        unique_ch = set(s)
        unique_ch_word = set()

        for word in wordDict:
            unique_ch_word.update(word)

        for ch in unique_ch:
            if ch not in unique_ch_word:
                return False

        d = [set() for _ in range(len(s))]

        for i in range(len(s), -1, -1):
            for word in wordDict:
                if len(word) > len(s) - i:
                    break

                if word == s[i:i+len(word)]:
                    d[i].add(len(word))


        def trace(cur: int) -> bool:
            res = False

            for i in d[cur]:
                if cur + i == len(s):
                    return True
                res |= trace(cur + i)
            d[cur] = set()

            return res

        if len(d[0]) == 0:
            return False

        return trace(0)

sol = Solution()
print(sol.wordBreak("leetcode", ["leet", "code"]))
print(sol.wordBreak("applepenapple", ["apple","pen"]))
print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
print(sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                    ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
print(sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]))
