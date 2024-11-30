from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0

        for i in range(1, int(len(words) / 2) + 1):
            in_left = (startIndex + i) % len(words)
            in_right = abs((len(words) + startIndex - i) % len(words))
            if words[in_left] == target or words[in_right] == target:
                return i

        return -1


sol = Solution()
# print(sol.closetTarget(words=["hello", "i", "am", "leetcode", "hello"], target="hello", startIndex=1))
# print(sol.closetTarget(words=["a", "b", "leetcode"], target="leetcode", startIndex=0))
# print(sol.closetTarget(words=["a", "b", "с", "d", 'e', "f"], target="d", startIndex=0))
print(sol.closetTarget(words=[
    "hsdqinnoha","mqhskgeqzr","zemkwvqrww","zemkwvqrww","daljcrktje","fghofclnwp","djwdworyka","cxfpybanhd","fghofclnwp","fghofclnwp"
], target="zemkwvqrww", startIndex=8))
