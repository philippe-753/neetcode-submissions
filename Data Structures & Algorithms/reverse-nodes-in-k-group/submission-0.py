# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], K: int) -> Optional[ListNode]:
        
        ll_len = 0
        cur = head
        while cur:
            ll_len += 1
            cur = cur.next
        
        N = ll_len // K
        cur = head

        dummy = ListNode(-1)
        group_prev = dummy
        for i in range(N):
            prev = None
            tail = cur
            for _ in range(K):
                temp = cur.next
                cur.next = prev

                prev = cur
                cur = temp

            group_prev.next = prev
            group_prev = tail
        
        group_prev.next = cur

        return dummy.next
            
        
            
            


        