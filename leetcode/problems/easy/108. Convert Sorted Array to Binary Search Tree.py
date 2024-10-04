# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if len(nums) == 1:
            return TreeNode(val=nums[0])

        def rec(left, right) -> Optional[TreeNode]:
            nonlocal nums

            if left > right:
                return None

            med = (right + left) // 2
            cur = TreeNode(val=nums[med])
            cur.left = rec(left, med - 1)
            cur.right = rec(med + 1, right)
            return cur

        return rec(0, len(nums) - 1)


sol = Solution()
nums = [i for i in range(10)]


def traversal(node):
    print(node.val)
    if node.left:
        traversal(node.left)
    if node.right:
        traversal(node.right)


root = sol.sortedArrayToBST(nums)
traversal(root)
