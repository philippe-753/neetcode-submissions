from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, k: int) -> int:
        
        adj = defaultdict(list)
        for a, b, time in times:
            adj[a].append([time, b])


        min_heap = [(0, k)] # time, node
        heapq.heapify(min_heap)
        visited = set()

        res = 0
        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue

            res = max(res, time)
            visited.add(node)
            for nei_time, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, [time + nei_time, nei])

        return res if len(visited) == N else -1


