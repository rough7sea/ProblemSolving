class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for e in s:
            if not e.isdigit():
                stack.append(e)
            elif s:
                stack.pop()
        return ''.join(stack)


sol = Solution()
print(sol.clearDigits('abc'))
