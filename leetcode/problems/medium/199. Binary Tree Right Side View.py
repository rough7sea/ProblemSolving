# Definition for a binary tree node.
from typing import List, Optional, Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)
            if len(res) < level:
                res.append(node.val)

            for child in [node.right, node.left]:
                if child:
                    queue.append([child, level + 1])

        return res
