# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 'L' means to go from a node to its left child node.
# 'R' means to go from a node to its right child node.
# 'U' means to go from a node to its parent node.


class Solution:
    # def getDirections_v1(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
    #     result = {}
    #     stack = [[root, '']]
    #
    #     while len(stack) > 0:
    #         node, path = stack.pop()
    #
    #         if node.val == startValue:
    #             result[startValue] = path
    #         elif node.val == destValue:
    #             result[destValue] = path
    #
    #         if len(result) == 2:
    #             break
    #
    #         if node.left:
    #             stack.append([node.left, path + 'L'])
    #
    #         if node.right:
    #             stack.append([node.right, path + 'R'])
    #
    #     start_path = result[startValue]
    #     dest_path = result[destValue]
    #
    #     i, y = 0, 0
    #     while i < len(start_path) and y < len(dest_path) and start_path[i] == dest_path[y]:
    #         i += 1
    #         y += 1
    #
    #     if i == y:
    #         return ('U' * (len(start_path) - i)) + dest_path[y:]
    #
    #     if len(dest_path) > len(start_path):
    #         return dest_path[y:]
    #
    #     return 'U' * (len(start_path) - i)

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def rec(node, val, path) -> bool:
            if node.val == val:
                return True

            if node.left and rec(node.left, val, path):
                path.append('L')
                return True

            if node.right and rec(node.right, val, path):
                path.append('R')
                return True
            return False

        start_path = []
        rec(root, startValue, start_path)
        dest_path = []
        rec(root, destValue, dest_path)

        while start_path and dest_path and start_path[- 1] == dest_path[- 1]:
            start_path.pop()
            dest_path.pop()

        return 'U' * len(start_path) + ''.join(dest_path[::-1])


sol = Solution()
print(sol.getDirections(
    TreeNode(4,
             TreeNode(1,
                      TreeNode(0, ),
                      TreeNode(2, right=TreeNode(3))),
             TreeNode(6,
                      TreeNode(5, ),
                      TreeNode(7, right=TreeNode(8)))),
    startValue=7,
    destValue=3
))  # UULRR
