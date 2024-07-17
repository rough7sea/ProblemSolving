# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cur = head
        result = [-1, -1]
        i = 1
        first = None
        prev = None
        while cur:
            if cur.next and cur.next.next:
                next_val = cur.next.val
                if ((cur.val < next_val and next_val > cur.next.next.val) or
                        (cur.val > next_val and next_val < cur.next.next.val)):
                    if first is None:
                        first = i
                        prev = i
                    else:
                        result[1] = i - first  # max
                        if result[0] == -1:
                            result[0] = i - prev
                        else:
                            result[0] = min(result[0], i - prev)  # min
                        prev = i

            cur = cur.next
            i += 1

        return result


sol = Solution()


def arr_to_Nodes(list: List[int]) -> Optional[ListNode]:
    head = None
    cur = None
    for e in list:
        if head is None:
            head = ListNode(e)
            cur = head
        else:
            cur.next = ListNode(e)
            cur = cur.next
    return head


print(sol.nodesBetweenCriticalPoints(arr_to_Nodes([5, 3, 1, 2, 5, 1, 2])))
