# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head.next
        # find the middle point.
        while fast and fast.next:
            if slow == fast:
                break
            fast = fast.next.next
            slow = slow.next
        

        mid = slow.next
        prev = slow.next = None
        # reverse second half.
        while mid:
            temp = mid.next
            mid.next = prev

            prev = mid
            mid = temp
        
        
        left = head
        rev = prev
        while rev:
            temp1, temp2 = left.next, rev.next
            left.next = rev
            rev.next = temp1

            left = temp1
            rev = temp2
        


