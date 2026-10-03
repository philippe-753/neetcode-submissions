# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        K = len(lists)
        dummy = ListNode(-1)
        res = dummy
        while True:
            min_idx = -1
            for i in range(K):
                if not lists[i]:
                    continue
                if min_idx == -1 or lists[i].val < lists[min_idx].val:
                    min_idx = i
                
            if min_idx == -1:
                break
            
            res.next = lists[min_idx]
            lists[min_idx] = lists[min_idx].next
            res = res.next

        return dummy.next
            
