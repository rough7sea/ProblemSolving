# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res = []
        def rec(node):
            if not node:
                return
            if node.left:
                rec(node.left)
            self.res.append(node.val)
            if node.right:
                rec(node.right)
        rec(root)

    def next(self) -> int:
        return self.res.pop(0)

    def hasNext(self) -> bool:
        return len(self.res) > 0
