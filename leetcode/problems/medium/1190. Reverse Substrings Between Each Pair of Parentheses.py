class Solution:
    def reverseParentheses(self, s: str) -> str:
        if len(s) == 1:
            return s

        stack = []
        current = ''
        for e in s:
            if e == '(':
                stack.append(current)
                current = ''
            elif e == ')':
                current = current[::-1]
                current = stack.pop() + current
            else:
                current += e

        return current


sol = Solution()
print(sol.reverseParentheses(s="(ed(et(oc))el)"))


# (ed(et(oc))el)
# (ed(etco)el)
# (edocteel)
# leetcode
