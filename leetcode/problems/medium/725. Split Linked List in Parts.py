# Definition for singly-linked list.
import math
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = 0
        node = head
        while node:
            size += 1
            node = node.next

        index = 0
        node = head
        res = []
        groups = k

        while index < size:
            groupSize = math.ceil((size - index) / groups)
            startNode = node

            index += 1
            for i in range(groupSize - 1):
                node = node.next
                index += 1
            res.append(startNode)

            nextNode = node.next
            node.next = None
            node = nextNode
            groups -= 1

        while groups > 0:
            res.append(None)
            groups -= 1
        return res


sol = Solution()
result = sol.splitListToParts(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10, ))),),),),),),),),
    2)

# result = sol.splitListToParts(
#     ListNode(1, ListNode(2, ListNode(3,),),),
#     5)

# result = sol.splitListToParts(
#     ListNode(1, ListNode(2,),),
# 4)

for l in result:
    n = l
    s = '['
    while n:
        s += f'{n.val} '
        n = n.next
    print(s+']')
