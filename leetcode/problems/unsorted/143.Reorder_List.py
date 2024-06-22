from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None:
            return
        queue = deque()
        current = head.next
        while current is not None:
            queue.append(current)
            current = current.next

        current = head
        left = False
        while len(queue) != 0:
            if left:
                left = False
                popleft = queue.popleft()
                current.next = popleft
                current = current.next
                current.next = None
            else:
                left = True
                pop_right = queue.pop()
                current.next = pop_right
                current = current.next
                current.next = None


sol = Solution()

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol.reorderList(head)

while head is not None:
    print(head.val)
    head = head.next

