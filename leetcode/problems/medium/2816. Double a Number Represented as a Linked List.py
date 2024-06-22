from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        val = ''
        while cur is not None:
            val += repr(cur.val)
            cur = cur.next
        new_val_string = repr(int(val) * 2)
        if len(new_val_string) > len(val):
            head = ListNode(1, head)

        cur = head
        for e in new_val_string:
            cur.val = e
            cur = cur.next

        return head


sol = Solution()
h = sol.doubleIt(ListNode(9, ListNode(4, ListNode(0, ListNode(4)))))
cur = h
while cur is not None:
    print(cur.val)
    cur = cur.next
