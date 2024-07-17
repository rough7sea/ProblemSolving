# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def delNodes_v1(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    #     map = dict()
    #     queue = [[root, None]]
    #
    #     while len(queue) > 0:
    #         node, parent = queue.pop(0)
    #         map[node.val] = [node, parent]
    #
    #         if node.right:
    #             queue.append([node.right, node])
    #
    #         if node.left:
    #             queue.append([node.left, node])
    #
    #     result = dict()
    #     result[root.val] = root
    #
    #     for e in to_delete:
    #         node, parent = map[e]
    #         if e in result:
    #             del result[e]
    #
    #         if parent:
    #             if parent.left and parent.left.val == e:
    #                 parent.left = None
    #             else:
    #                 parent.right = None
    #
    #         if node.left:
    #             result[node.left.val] = node.left
    #
    #         if node.right:
    #             result[node.right.val] = node.right
    #
    #     return result.values()


        def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
            to_delete = set(to_delete)
            result = []

            def rec(node, to_delete) -> Optional[TreeNode]:
                if not node:
                    return None

                if node.right:
                    node.right = rec(node.right,  to_delete)

                if node.left:
                    node.left = rec(node.left, to_delete)

                if node.val in to_delete:
                    if node.right:
                        result.append(node.right)
                    if node.left:
                        result.append(node.left)
                    return None
                else:
                    return node

            node = rec(root, to_delete)
            if node:
                result.append(node)
            return result

