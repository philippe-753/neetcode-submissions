import heapq
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Time: O(N long N) Space: O(N) - > O(klog N ), Space: O(N)
        min_heap = []
        for x, y in points:
            dis = x**2 + y**2
            min_heap.append([dis, x, y])

        heapq.heapify(min_heap)
        res = []
        for i in range(k):
            min_val, x, y= heapq.heappop(min_heap)
            res.append([x, y])
        return res



        

        
