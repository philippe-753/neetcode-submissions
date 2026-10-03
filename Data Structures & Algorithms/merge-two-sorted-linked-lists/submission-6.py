# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0)
        dummy = head

        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next

            else:
                dummy.next = list2
                list2 = list2.next
            
            dummy = dummy.next

        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2
        
        return head.next































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
            

