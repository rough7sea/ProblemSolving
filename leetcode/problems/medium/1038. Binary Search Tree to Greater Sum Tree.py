# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sum = 0

        def rec(node: TreeNode):
            nonlocal sum

            if node.right:
                rec(node.right)

            sum += node.val
            node.val = sum

            if node.left:
                rec(node.left)

        rec(root)
        return root


sol = Solution()
new = sol.bstToGst(
    TreeNode(4,
             TreeNode(1,
                      TreeNode(0, ),
                      TreeNode(2, right=TreeNode(3))),
             TreeNode(6,
                      TreeNode(5, ),
                      TreeNode(7, right=TreeNode(8))))
)

stack = [new]
while len(stack) > 0:
    node = stack.pop(0)
    print(node.val)
    if node.right is not None:
        stack.append(node.right)
    if node.left is not None:
        stack.append(node.left)
