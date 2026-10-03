from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], N: int) -> int:
        task_freq = Counter(tasks)
        max_heap = [-freq for freq in task_freq.values()]
        heapq.heapify(max_heap) 
    
        queue = deque([]) # updated_value, available time.        
        
        time = 0
        while queue or max_heap:            
            time += 1

            if max_heap:
                cur = 1 + heapq.heappop(max_heap)
                if cur < 0:
                    queue.append([cur, time+N])
            else:
                time = queue[0][1]
            
            if queue and queue[0][1] <= time:
                cur, idle = queue.popleft()
                heapq.heappush(max_heap, cur)
        
        return time
            
                    


        
