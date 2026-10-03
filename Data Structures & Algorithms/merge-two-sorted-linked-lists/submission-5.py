# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(val=0)
        cur = dummy
        l = list1
        r = list2

        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next

        if l:
            cur.next = l

        if r:
            cur.next = r
        
        return dummy.next
                































        # dummy = ListNode(val=-1)
        # ans = dummy
        # cur_1 = list1
        # cur_2 = list2

        # while cur_1 or cur_2:
        #     if not cur_2:
        #         dummy.next = cur_1 
        #         cur_1 = cur_1.next
        #     elif not cur_1:
        #         dummy.next = cur_2
        #         cur_2 = cur_2.next
        #     elif cur_1.val < cur_2.val:
        #         dummy.next = cur_1 
        #         cur_1 = cur_1.next 
        #     else:
        #         dummy.next = cur_2
        #         cur_2 = cur_2.next

        #     dummy = dummy.next

        # return ans.next
            

