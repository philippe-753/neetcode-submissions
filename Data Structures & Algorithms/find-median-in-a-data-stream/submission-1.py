import heapq
import math

class MedianFinder:

    def __init__(self):
        self.small_heap = [] # max_heap
        self.large_heap = [] # min_heap

    def addNum(self, num: int) -> None:
        if self.large_heap and num >= self.large_heap[0]:
            heapq.heappush(self.large_heap, num)
        else:
            heapq.heappush(self.small_heap, -num)
        self._rebalance()
        
    def _rebalance(self) -> None:
        while abs(len(self.small_heap) - len(self.large_heap)) > 1:
            if len(self.small_heap) > len(self.large_heap):
                num  = - heapq.heappop(self.small_heap)
                heapq.heappush(self.large_heap, num)
            else:
                num = - heapq.heappop(self.large_heap)
                heapq.heappush(self.small_heap, num)


    def findMedian(self) -> float:
        if len(self.small_heap) > len(self.large_heap):
            median = - self.small_heap[0]
        elif len(self.small_heap) < len(self.large_heap):
            median = self.large_heap[0]
        else:
            median = (self.large_heap[0] - self.small_heap[0]) / 2
        return median


"""
large:
[
    1, 
]


small:
[
    4,
]


"""