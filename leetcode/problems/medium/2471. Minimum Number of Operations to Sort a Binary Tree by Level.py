# Definition for a binary tree node.
from heapq import heappush, heappop
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [(root, 0)]
        cur_level = -1
        arr = None
        heap = None
        el_to_index = None
        res = 0

        while queue:
            node, level = queue.pop(0)
            if level != cur_level:
                if cur_level > -1:
                    res += self.countSwaps(arr, heap, el_to_index)
                i = 0
                arr = []
                heap = []
                el_to_index = dict()
                cur_level = level

            arr.append(node.val)
            heappush(heap, -node.val)
            el_to_index[node.val] = len(arr) - 1

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        res += self.countSwaps(arr, heap, el_to_index)

        return res

    def countSwaps(self, arr: list, heap: list, el_to_index: dict) -> int:
        count = 0
        print(arr)

        for i in range(len(arr) - 1, -1, -1):
            val = heappop(heap)
            val = -val
            j = el_to_index[val]
            if arr[i] != val:
                arr[i], arr[j] = arr[j], arr[i]
                el_to_index[arr[j]] = j
                count += 1
        return count


sol = Solution()
# print(sol.minimumOperations(
#     TreeNode(1,
#              left=TreeNode(4,
#                            left=TreeNode(7, ),
#                            right=TreeNode(6, ),
#                            ),
#              right=TreeNode(3,
#                             left=TreeNode(8, left=TreeNode(9, ), ),
#                             right=TreeNode(5, left=TreeNode(10, ), ),
#                             )
#              )
# ))

print(sol.minimumOperations(
    TreeNode(49,
             left=TreeNode(45,
                           left=TreeNode(20, left=TreeNode(27, ), ),
                           right=TreeNode(46, ),
                           ),
             right=TreeNode(1,
                            left=TreeNode(15, left=TreeNode(25, ), ),
                            right=TreeNode(39, ),
                            )
             )
))
