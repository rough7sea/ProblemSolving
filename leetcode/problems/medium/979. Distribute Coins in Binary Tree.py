# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#       0
#   2           3
# 0  0       null null
# 1

# 1 + 1 + 3
# 1 + 3 + 3


#       0
#   3           2
# 0  0       null null
# 1

# 1 + 1 + 1


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        #move coins to parent DFS
        def f(root, parent):
            if root == None:
                return 0
            moves = f(root.left, root) + f(root.right, root)
            x = root.val - 1
            if parent != None:
                parent.val += x
            moves += abs(x)
            return moves

        return f(root, None)

    # class TreeNodeFacade:
    #     def __init__(self, parent=None, val=0, left=None, right=None):
    #         self.parent = parent
    #         self.left = left
    #         self.right = right
    #         self.val = val
    #         self.visited = 0


    # def distributeCoins(self, root: Optional[TreeNode]) -> int:
    #     queue = [[root, TreeNodeFacade(val=root.val)]]
    #     coin_nodes = []
    #
    #     while len(queue) > 0:
    #         element = queue.pop(0)
    #         cur = element[0]
    #         facade = element[1]
    #
    #         if cur.val > 1:
    #             coin_nodes.append(facade)
    #
    #         if cur.left is not None:
    #             left_facade = TreeNodeFacade(val=cur.left.val, parent=facade)
    #             facade.left = left_facade
    #             queue.append([cur.left, left_facade])
    #
    #         if cur.right is not None:
    #             right_facade = TreeNodeFacade(val=cur.right.val, parent=facade)
    #             facade.right = right_facade
    #             queue.append([cur.right, right_facade])
    #
    #     if len(coin_nodes) == 0:
    #         return 0
    #
    #     # print(facadeRoot)
    #
    #     result_steps = 0
    #     visited_index = 1
    #
    #     while len(coin_nodes) > 0:
    #         coin_node = coin_nodes.pop(0)
    #         coin_node.visited = visited_index
    #         queue = [[coin_node, 1]]
    #
    #         while coin_node.val > 1:
    #             element = queue.pop(0)
    #             cur = element[0]
    #             steps = element[1]
    #
    #             node_parent = cur.parent
    #             if node_parent is not None:
    #                 if node_parent.visited != visited_index:
    #                     if node_parent.val < 1:
    #                         node_parent.val = 1
    #                         coin_node.val -= 1
    #                         result_steps += steps
    #                     node_parent.visited = visited_index
    #                     queue.append([node_parent, steps + 1])
    #
    #             if coin_node.val == 1:
    #                 break
    #
    #             node_left = cur.left
    #             if node_left is not None:
    #                 if node_left.visited != visited_index:
    #                     if node_left.val < 1:
    #                         node_left.val = 1
    #                         coin_node.val -= 1
    #                         result_steps += steps
    #                     node_left.visited = visited_index
    #                     queue.append([node_left, steps + 1])
    #
    #             if coin_node.val == 1:
    #                 break
    #
    #             node_right = cur.right
    #             if node_right is not None:
    #                 if node_right.visited != visited_index:
    #                     if node_right.val < 1:
    #                         node_right.val = 1
    #                         coin_node.val -= 1
    #                         result_steps += steps
    #                     node_right.visited = visited_index
    #                     queue.append([node_right, steps + 1])
    #
    #             if coin_node.val == 1:
    #                 break
    #
    #         visited_index += 1
    #
    #     return result_steps


sol = Solution()
tree = TreeNode(6, left=TreeNodeFacade(0, left=TreeNodeFacade(0, left=TreeNodeFacade(0))),
                right=TreeNodeFacade(0, left=TreeNodeFacade(0)))
print(sol.distributeCoins(tree))
