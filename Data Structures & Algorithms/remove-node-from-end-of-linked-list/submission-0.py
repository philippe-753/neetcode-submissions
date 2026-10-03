# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], N: int) -> Optional[ListNode]:

        cur = head
        list_len: int = 0
        while cur:
            cur = cur.next
            list_len += 1
        
        N_start = list_len - N
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy

        for i in range(N_start):
            cur = cur.next
        
        cur.next = cur.next.next
        return dummy.next



        