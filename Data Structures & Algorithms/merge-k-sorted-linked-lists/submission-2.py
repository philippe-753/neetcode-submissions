# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        K = len(lists)
        dummy = ListNode(0)
        cur = dummy

        while True:
            min_val = -float("inf")
            for i in range(K):
                if not lists[i]:
                    continue
                if min_val == -float("inf") or lists[i].val < lists[min_val].val:
                    min_val = i

            if min_val == -float("inf"):
                break

            min_list = lists[min_val]
            cur.next = min_list
            lists[min_val] = lists[min_val].next
            cur = cur.next
            
        return dummy.next
                


                    

        
            


