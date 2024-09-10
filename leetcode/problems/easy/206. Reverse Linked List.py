# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = head
        node = head.next

        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        # prev - node - next_node
        head.next = None
        return prev


sol = Solution()
print(sol.reverseList(
    ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,)))))
))