# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Leet codes defines a height-balanced binary tree as:
# a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# for better understanding, the tree is balanced if the difference between left subtree and right subtree is -1 or 0 or 1 (anyone).


# Based on this, if have to look at the max depth of the
# left sub tree from the root (5) and the max depth
# of the right sub tree from the root (4), so it's considered balanced.


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        balanced = True
        
        def rec(node) -> int:
            if not node:
                return 1
            leftDepth = rec(node.left)
            rightDepth = rec(node.right)
            if abs(leftDepth - rightDepth) > 1:
                nonlocal balanced
                balanced = False
            return max(leftDepth, rightDepth) + 1
        rec(root)
        return balanced


sol = Solution()
print(sol.isBalanced(
    TreeNode(3,
             TreeNode(9, ),
             TreeNode(20,
                      TreeNode(15, ),
                      TreeNode(17, ))
             )
))
