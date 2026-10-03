class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        min_heap = []
        cur_cap = 0

        for trip in trips:
            while min_heap and min_heap[0][0] <= trip[1]:
                _, last_cap = heapq.heappop(min_heap)
                cur_cap -= last_cap
            
            cur_cap += trip[0]

            if cur_cap > capacity:
                return False
            
            heapq.heappush(min_heap, [trip[2], trip[0]])
        
        return True




        
