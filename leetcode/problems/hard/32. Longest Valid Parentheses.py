class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
                continue

            if not stack:
                stack.append(i)
                continue

            if s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)

        if not stack:
            return len(s)

        res = 0
        stack.append(len(s))
        stack.insert(0, -1)
        for i in range(len(stack)-2, -1, -1):
            res = max(res, stack[i+1] - stack[i] - 1)
        return res


sol = Solution()
print(sol.longestValidParentheses(s='(()'))
print(sol.longestValidParentheses(s=")()())"))
print(sol.longestValidParentheses(s="()())()()()())()()())"))

#
# ()())()()()())()()())



