import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        N = len(tasks)
        tasks = [[start, t_taken, idx] for idx, (start, t_taken) in enumerate(tasks)]
        tasks.sort()
        
        min_heap = []
        time = 0
        res = []
        i = 0
        while i < N or min_heap:
            while i < N and tasks[i][0] <= time:
                heapq.heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if min_heap:
                t_taken, idx = heapq.heappop(min_heap)
                time += t_taken
                res.append(idx)
            else:
                time = tasks[i][0]
            

        
        return res


