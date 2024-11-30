# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node_1 = l1
        node_2 = l2
        plus_one = 0

        result = None
        cur_node = None

        while node_1 is not None or node_2 is not None or plus_one > 0:
            if node_1 is not None:
                node_1_val = node_1.val
                node_1 = node_1.next
            else:
                node_1_val = 0

            if node_2 is not None:
                node_2_val = node_2.val
                node_2 = node_2.next
            else:
                node_2_val = 0

            sum = node_1_val + node_2_val + plus_one

            if cur_node is None:
                result = ListNode()
                cur_node = result
            else:
                cur_node.next = ListNode()
                cur_node = cur_node.next

            plus_one = sum // 10
            cur_node.val = sum % 10
        return result


sol = Solution()
list_1 = ListNode(2, ListNode(4, ListNode(3)))
list_2 = ListNode(5, ListNode(6, ListNode(4)))
numbers = sol.addTwoNumbers(list_1, list_2)


str = ''
while numbers is not None:
    str += '[' + numbers.val.__str__() + '] -> '
    numbers = numbers.next

print(str)