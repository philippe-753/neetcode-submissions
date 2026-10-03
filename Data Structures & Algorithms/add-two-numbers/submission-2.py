# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur_l1 = l1
        cur_l2 = l2
        res = ListNode(0)
        cur_sum = res

        carry = 0
        while cur_l1 or cur_l2 or carry:
            l1_val = cur_l1.val if cur_l1 else 0
            l2_val = cur_l2.val if cur_l2 else 0

            # Net digit
            val_sum = l1_val + l2_val + carry
            carry = val_sum // 10
            val_sum %= 10
            cur_sum.next = ListNode(val_sum)
            
            # update
            cur_l1 = cur_l1.next if cur_l1 else None
            cur_l2 = cur_l2.next if cur_l2 else None
            cur_sum = cur_sum.next
        
        return res.next
            