# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        maxNode = root
        max_node_level = 0
        nodeLink = root
        max_link_level = 0

        def rec(node, level) -> int:
            nonlocal maxNode
            nonlocal max_node_level
            nonlocal max_link_level
            nonlocal nodeLink
            if not node:
                return 0

            if not node.left and not node.right:
                if max_node_level < level:
                    max_node_level = level
                    maxNode = node
                return level

            level_left = 0
            if node.left:
                level_left = rec(node.left, level + 1)

            level_right = 0
            if node.right:
                level_right = rec(node.right, level + 1)

            if level_left > 0 and level_left == level_right:
                if level_left == max_node_level:
                    nodeLink = node
                    max_node_level = level_left
                    max_link_level = level_left
                return level_left

            return max(level_left, level_right)

        rec(root, 0)

        if max_link_level >= max_node_level:
            return nodeLink
        return maxNode


sol = Solution()
res = sol.lcaDeepestLeaves(
    root=
    TreeNode(3,
             TreeNode(5,
                      TreeNode(6, ),
                      TreeNode(2,
                               TreeNode(7, ),
                               TreeNode(4, ),),
                      ),
             TreeNode(1,
                      TreeNode(0, ),
                      TreeNode(8, ),)
             ))
print(res.val)


res = sol.lcaDeepestLeaves(
    root=
    TreeNode(3,
             TreeNode(5,
                      TreeNode(6, ),
                      TreeNode(2,
                               TreeNode(7, ),
                               TreeNode(4, ),),
                      ),
             TreeNode(1,
                      TreeNode(0,
                               TreeNode(10, ),),
                      TreeNode(8, ),)
             ))
print(res.val)

#
# res = sol.lcaDeepestLeaves(
#     root=
#     TreeNode(0,
#              TreeNode(1,
#                       TreeNode(2,),
#                       ),
#              TreeNode(3,)
#              ))
#
# print(res.val)
