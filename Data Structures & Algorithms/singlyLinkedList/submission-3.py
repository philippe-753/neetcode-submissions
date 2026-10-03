class LinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    
    def __init__(self):
        self.linked_list = None # no val


    def get(self, index: int) -> int:
        
        cur = self.linked_list

        i = 0
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1

        return -1


    def insertHead(self, val: int) -> None:
        self.linked_list = LinkedNode(val, next=self.linked_list)


    def insertTail(self, val: int) -> None:
        cur = self.linked_list

        if self.linked_list is None: #  edge case
            self.linked_list = LinkedNode(val)
            return

        while cur and cur.next:
            cur = cur.next
        cur.next = LinkedNode(val, next=None)
        
        

    def remove(self, index: int) -> bool:

        if index == 0:
            if not self.linked_list:
                return False
            self.linked_list = self.linked_list.next
            return True
        
        # 1->2->3->None
        cur = self.linked_list
        prev = self.linked_list
        i = 0
        while cur and cur.next and i < index:
            prev = cur
            cur = cur.next
            i += 1

        if i < index:
            return False

        prev.next = cur.next
        return True

    def getValues(self) -> List[int]:
        vals = []

        cur = self.linked_list
        while cur:
            vals.append(cur.val)
            cur = cur.next

        return vals
        
