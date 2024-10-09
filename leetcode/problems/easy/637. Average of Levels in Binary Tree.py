# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = [(root, 0)]
        prev_level = 0
        vals = []

        while queue:
            node, level = queue.pop(0)
            if prev_level < level:
                res.append(sum(vals) / len(vals))
                vals = []
                prev_level = level
            vals.append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        res.append(sum(vals) / len(vals))
        return res
