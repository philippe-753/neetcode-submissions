import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for a, b, price in flights:
            adj[a].append([b, price])

        
        mean_heap = []
        mean_heap.append([0, 0, src]) # total_cost, number of stops, node

        while mean_heap:
            cost, stops, node = heapq.heappop(mean_heap)

            if node == dst:
                return cost
            
            if stops > k:
                continue
            
            for nei, nei_cost in adj[node]:
                heapq.heappush(mean_heap, [cost+nei_cost, stops+1, nei])
        
        return -1