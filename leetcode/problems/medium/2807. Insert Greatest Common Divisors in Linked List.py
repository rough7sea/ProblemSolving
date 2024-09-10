from math import gcd
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            child = node.next
            new_val = gcd(node.val, child.val)
            new_node = ListNode(new_val, child)
            node.next = new_node
            node = child
        return head

