# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        parentToRemove = head
        node = head
        count = 0
        while node:
            if n < count:
                parentToRemove = parentToRemove.next
            node = node.next
            count += 1

        if count == 1:
            return None

        if count == n:
            return head.next

        toRemove = parentToRemove.next
        if toRemove:
            parentToRemove.next = toRemove.next
        else:
            parentToRemove.next = None
        return head


sol = Solution()
# res = sol.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ))))), 2)
# res = sol.removeNthFromEnd(ListNode(1, ListNode(2, )), 1)
res = sol.removeNthFromEnd(ListNode(1, ListNode(2, )), 2)

next = res
while next:
    print(next.val)
    next = next.next


# head = [1,2,3,4,5,6,7,8,9,10], n = 4
# 7 to remove
# 6 - parent


