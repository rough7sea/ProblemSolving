# Definition for a binary tree node.
from heapq import heappush, heappop
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def rec(node, val_set: set, heap: list):
            if not node:
                return

            if node.val not in val_set:
                val_set.add(node.val)
                heappush(heap, -node.val)
                if len(heap) > 2:
                    heappop(heap)
            rec(node.left, val_set, heap)
            rec(node.right, val_set, heap)
        heap = []
        rec(root, set(), heap)
        if len(heap) < 2:
            return -1
        return -heappop(heap)

