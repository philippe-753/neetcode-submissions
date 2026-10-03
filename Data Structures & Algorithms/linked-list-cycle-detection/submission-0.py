# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head and not head.next or not head.next.next:
            return False        

        slow = head.next
        fast = head.next.next

        while fast:

            if slow == fast:
                return True
            
            if not fast.next or not fast.next.next:
                return False
            else:
                fast = fast.next.next
                slow = slow.next

        return False
            
