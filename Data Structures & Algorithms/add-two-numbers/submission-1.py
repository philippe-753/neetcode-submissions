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

        prev = 0
        while cur_l1 or cur_l2:
            l1_val, l2_val = 0, 0
            if cur_l1:
                l1_val = cur_l1.val
                cur_l1 = cur_l1.next
            if cur_l2:
                l2_val = cur_l2.val
                cur_l2 = cur_l2.next

            val_sum = l1_val + l2_val + prev
            if val_sum >= 10:
                prev = val_sum // 10
                val_sum %= 10
            else:
                prev = 0
            
            cur_sum.next = ListNode(val_sum)
            cur_sum = cur_sum.next

        if prev:
            cur_sum.next = ListNode(prev)

        
        return res.next
            