import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) >= 2:
            max_1 = heapq.heappop(max_heap)
            max_2 = heapq.heappop(max_heap)

            if max_1 - max_2 != 0:
                heapq.heappush(max_heap, max_1-max_2)
        
        if len(max_heap) == 1:
            return -max_heap[0]
        if len(max_heap) == 0:
            return 0

            
        
