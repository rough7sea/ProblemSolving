from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        cur_node = None
        prev = None
        node = head
        while node:
            if node.val == 0:
                if cur_node:
                    prev = cur_node
                    cur_node.next = ListNode(0)
                    cur_node = cur_node.next
                else:
                    cur_node = ListNode(0)
                    result = cur_node
            else:
                cur_node.val += node.val
            node = node.next

        prev.next = None
        return result


sol = Solution()
# [0,3,1,0,4,5,2,0]
sol.mergeNodes(
    ListNode(0,
             ListNode(3,
                      ListNode(1,
                               ListNode(0,
                                        ListNode(4,
                                                 ListNode(5,
                                                          ListNode(2,
                                                                   ListNode(0, )))))))))