import heapq
import math

class MedianFinder:
    def __init__(self):
        self.small = [] # max_heap
        self.big = [] # min_heap

    def addNum(self, num: int) -> None:
        if not self.small and not self.big:
            heapq.heappush(self.small, -num)
        
        elif self.small and not self.big:
            heapq.heappush(self.big, num)
        
        elif num > -self.small[0]:
            heapq.heappush(self.big, num)
        else:
            heapq.heappush(self.small, -num)
        
        self._rebalance()
        
        # re-balance:
    def _rebalance(self):
        if not self.big or not self.small:
            return None

        elif self.big[0] < -self.small[0]:
            val_small, val_big = -heapq.heappop(self.small), -heapq.heappop(self.big)
            heapq.heappush(self.small, val_big)
            heapq.heappush(self.big, val_small)
        
        elif len(self.small) > len(self.big) + 1:
            pop_val = -heapq.heappop(self.small)
            heapq.heappush(self.big, pop_val)
        
        elif len(self.big) > len(self.small) + 1:
            pop_val = -heapq.heappop(self.big)
            heapq.heappush(self.small, pop_val)


    def findMedian(self) -> float:
        if not self.big or len(self.small) > len(self.big):
            return -self.small[0]
        elif len(self.big) > len(self.small):
            return self.big[0]
        else:
            return float(-self.small[0] + self.big[0])/ 2


"""
sm = [5] # max_heap 
bg = [5, 6] # min_heap



"""