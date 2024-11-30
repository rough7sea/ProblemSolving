class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        if sentence[0] != sentence[len(sentence) - 1]:
            return False

        i = 0
        while i < len(sentence):
            if sentence[i] != ' ':
                i += 1
                continue
            if sentence[i - 1] != sentence[i + 1]:
                return False
        return True
