from collections import defaultdict, Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        subset_counter = defaultdict(int)

        for word in words2:
            word_counter = defaultdict(int)
            for c in word:
                word_counter[c] += 1

            for key in word_counter.keys():
                subset_counter[key] = max(subset_counter[key], word_counter[key])
        res = []
        for word in words1:
            word_counter = Counter(word)
            universal = True
            for key in subset_counter.keys():
                if word_counter[key] < subset_counter[key]:
                    univerdsal = False
                    break
            if universal:
                res.append(word)
        return res

