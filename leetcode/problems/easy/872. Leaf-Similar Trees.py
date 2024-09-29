# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def extractNextLeaf(self, treeDQ: List[TreeNode]) -> Optional[TreeNode]:
        while treeDQ:
            node = treeDQ.pop()
            if not node.left and not node.right:
                return node
            if node.right:
                treeDQ.append(node.right)
            if node.left:
                treeDQ.append(node.left)
        return None

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1DQ = [root1]
        tree2DQ = [root2]

        while tree1DQ or tree2DQ:
            leaf1 = self.extractNextLeaf(tree1DQ)
            leaf2 = self.extractNextLeaf(tree2DQ)

            if (not leaf1 and leaf2) or (leaf1 and not leaf2):
                return False
            if leaf1.val != leaf2.val:
                return False

        if len(tree1DQ) != len(tree2DQ):
            return False

        return True
