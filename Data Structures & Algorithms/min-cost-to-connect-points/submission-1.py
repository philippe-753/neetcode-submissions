from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points_dis = defaultdict(list)

        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points):
                if (x1, y1) == (x2, y2):
                    continue
                man_dis = abs(x1-x2) + abs(y1-y2)
                points_dis[i].append((man_dis, j))
        
        # print("points_dis", points_dis)

        min_heap = []
        visited = set()
        min_heap.append([0, 0]) # total_cost, cur_node, 
        heapq.heapify(min_heap)
        total_cost = 0
        while min_heap:
            cost, node = heapq.heappop(min_heap)
            # print("---")
            # print("node:", node)
            # print("cost", cost)
            if node in visited:
                continue

            total_cost += cost
            visited.add(node)
            if len(visited) == len(points):
                return total_cost
            
            for nc, nei in points_dis[node]:
                if nei not in visited:
                    # print("nei, nc", nei, nc)
                    heapq.heappush(min_heap, ([nc, nei]))
        
        return -1


