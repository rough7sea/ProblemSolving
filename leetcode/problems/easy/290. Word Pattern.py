class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map = dict()
        word_set = set()
        i = 0
        j = 0
        word_split = s.split()
        if len(word_split) != len(pattern):
            return False
        while i < len(pattern):
            word = word_split[i]
            p = pattern[i]
            if p not in map:
                map[p] = word
                if word in word_set:
                    return False
                word_set.add(word)
            if word != map[p]:
                return False
            i += 1
            j += 1

        return True


sol = Solution()
print(sol.wordPattern(pattern='abba', s="dog cat cat dog"))
