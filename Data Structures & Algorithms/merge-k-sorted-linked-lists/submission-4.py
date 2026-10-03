# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        N = len(lists)
        res = ListNode(0)
        cur = res
        while True:
            min_val, min_idx = float("inf"), -1
            for i in range(N):
                if not lists[i]:
                    continue
                
                node = lists[i]
                if node.val < min_val:
                    min_val, min_idx = node.val, i
            
            if min_val ==  float("inf"):
                break
            # Point to min val
            cur.next = lists[min_idx] 
            # Update
            lists[min_idx] = lists[min_idx].next
            cur = cur.next
        
        return res.next