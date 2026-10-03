from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, k: int) -> int:
        
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((t, v)) # time, next node.

        min_heap = []
        min_heap.append((0, k))
        heapq.heapify(min_heap)
        visited = set()
        visited.add(k)
        count = 0
        while min_heap:
            time, node = heapq.heappop(min_heap)
            print()
            visited.add(node)
            if len(visited) == N:
                return time
            
            for nt, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (time+nt, nei))
        return -1

            

    
    

