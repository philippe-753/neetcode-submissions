class LinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    
    def __init__(self):

        # 0->1->2->3
        #[HEAD] ---> [ Node ] ---> [ Node ] ---> [ Node ] ---> [TAIL]
        self.head = None
        self.tail = None


    def get(self, index: int) -> int:
        cur = self.head # 0->None
        i = 0
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i+= 1
        return -1


    def insertHead(self, val: int) -> None:
        new_node = LinkedNode(val, next=self.head) # 5->1->None
        self.head = new_node
        if self.tail is None:
            self.tail = new_node


    def insertTail(self, val: int) -> None:

        new_head = LinkedNode(val, next=None)
        # case 1: Inserting at tail when head and tail are None.
        if self.tail is None: 
            self.tail = new_head
            self.head = new_head # if tail is None then head is None too.
            return
        # case 2: Tail and head are not None.
        self.tail.next = new_head
        self.tail = self.tail.next # Update tail to point to new val.


    def remove(self, index: int) -> bool:
        # case 1: i == 0
        # case 2: 1->5->3->None
        # case 3: i>= index.

        if self.head is None:
            return False
        
        # case 1
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True

        cur = self.head
        prev = self.head
        i = 0
        # case 2:
        while cur and i < index:
            prev = cur
            cur = cur.next
            i+= 1
        
        # case 3
        if cur is None:
            return False

        prev.next = cur.next

        if cur == self.tail:
            self.tail = prev
        return True


    def getValues(self) -> List[int]:
        vals = []
        cur = self.head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals

        
        
