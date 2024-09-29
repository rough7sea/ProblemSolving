# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        def rec(node, path) -> str:
            path = chr(97 + node.val) + path

            if not node.left and not node.right:
                return path

            if not node.left:
                return rec(node.right, path)

            if not node.right:
                return rec(node.left, path)

            return min(rec(node.left, path), rec(node.right, path))

        return rec(root, "")

sol = Solution()
sol.smallestFromLeaf(None)
