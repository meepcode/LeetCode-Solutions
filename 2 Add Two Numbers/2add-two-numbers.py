# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        result = None
        cur_node = None
        while not l1 is None or not l2 is None or remainder != 0:
            if l1 is None:
                val1 = 0
            else:
                val1 = l1.val
            
            if l2 is None:
                val2 = 0
            else:
                val2 = l2.val

            old_node = cur_node
            cur_node = ListNode((val1 + val2 + remainder) % 10, None)
            
            if result is None:
                result = cur_node
            else:
                old_node.next = cur_node

            print(result)

            if val1 + val2 + remainder >= 10:
                remainder = 1
            else:
                remainder = 0

            if not l1 is None:
                l1 = l1.next
            
            if not l2 is None:
                l2 = l2.next
            
        return result
        