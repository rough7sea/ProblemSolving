# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        parents = {}
        nodes = {}

        for parentVal, childVal, isLeft in descriptions:
            if parentVal in nodes:
                parent = nodes[parentVal]
            else:
                parent = TreeNode(parentVal)
                nodes[parentVal] = parent
                parents[parentVal] = parent

            if childVal in nodes:
                child = nodes[childVal]
                if childVal in parents:
                    parents.pop(childVal)
            else:
                child = TreeNode(childVal)
                nodes[childVal] = child

            if isLeft == 1:
                parent.left = child
            else:
                parent.right = child

        return set(parents.values()).pop()

sol = Solution()
tree = sol.createBinaryTree(descriptions=[[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]])
print(tree)
