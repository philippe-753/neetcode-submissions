import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        N = len(points)
        max_heap = []
        heapq.heapify(max_heap)

        for x, y in points:
            dis = x**2 + y**2
            heapq.heappush(max_heap, [-dis, x, y])

            if len(max_heap) > K:
                heapq.heappop(max_heap)
        
        res = [[x, y] for dis, x, y in max_heap]
        return res
            

    