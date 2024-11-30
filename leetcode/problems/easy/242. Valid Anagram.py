from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cntS = Counter(s)
        cntT = Counter(t)
        if len(cntS) != len(cntT):
            return False

        for k in cntS.keys():
            if cntS[k] != cntT[k]:
                return False
        return True