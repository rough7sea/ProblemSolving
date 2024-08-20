# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def cleanDist(nodes, distance):
    newDict = {}
    for key in nodes:
        if key + 1 < distance:
            newDict[key + 1] = nodes[key]
    return newDict


def calculate(nodes_right, nodes_left, distance) -> int:
    count = 0
    for rd in nodes_right:
        for ld in nodes_left:
            if rd + ld <= distance:
                count += nodes_right[rd] * nodes_left[ld]
    return count


def merge(nodes_right, nodes_left, distance):
    merge = {}
    for key in nodes_right:
        if key in nodes_left:
            if key + 1 < distance:
                merge[key + 1] = nodes_right[key] + nodes_left[key]
            del nodes_left[key]
        else:
            merge[key + 1] = nodes_right[key]

    for key in nodes_left:
        if key + 1 < distance:
            merge[key + 1] = nodes_left[key]
    return merge


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if distance == 1:
            return 0

        self.count = 0

        def rec(node: TreeNode) -> dict:
            if not node.right and not node.left:
                return {1: 1}  # dest, count

            nodes_right = {}
            if node.right:
                nodes_right = rec(node.right)

            nodes_left = {}
            if node.left:
                nodes_left = rec(node.left)

            if len(nodes_right) > 0 and len(nodes_left) > 0:
                self.count += calculate(nodes_right, nodes_left, distance)
                return merge(nodes_right, nodes_left, distance)
            elif len(nodes_right) > 0:
                return cleanDist(nodes_right, distance)
            else:
                return cleanDist(nodes_left, distance)

        rec(root)
        return self.count


sol = Solution()
# print(sol.countPairs(
#     TreeNode(4,
#              TreeNode(1,
#                       TreeNode(0, ),
#                       TreeNode(2,
#                                TreeNode(3),
#                                TreeNode(42))),
#              TreeNode(6,
#                       TreeNode(5,
#                               ),
#                       TreeNode(7,
#                                TreeNode(8),
#                                TreeNode(42)
#                                ))),
#     3
# ))


# [15, 66,55, 97,60,12,56, null,54,null,49,null,9,null,null, null,null,null,90]
print(sol.countPairs(
    TreeNode(15,
             TreeNode(66,
                      TreeNode(97, right = TreeNode(54,)),
                      TreeNode(60,
                               right = TreeNode(49, right = TreeNode(90 )))),
             TreeNode(55,
                      TreeNode(12,right = TreeNode(9)),
                      TreeNode(56))),
    5
))
