# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def rec(node, path) -> List[int]:
            if not node:
                return []
            if not node.left and not node.right and node.val + path == targetSum:
                nonlocal res
                res.append([node.val])
                return [len(res) - 1]
            leafRes = rec(node.left, path + node.val)
            leafRes.extend(rec(node.right, path + node.val))
            if len(leafRes) > 0:
                nonlocal res
                for i in leafRes:
                    res[i].insert(0, node.val)
            return leafRes

        rec(root, 0)

        return res
