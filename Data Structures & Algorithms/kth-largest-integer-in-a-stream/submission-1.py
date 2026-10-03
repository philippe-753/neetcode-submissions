import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        self._heap_to_k_elements()
        
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        self._heap_to_k_elements()
        return self.min_heap[0]
    
    def _heap_to_k_elements(self):
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)


        
