import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        N = len(tasks)
        min_heap, res = [], []
        tasks = [[enq_time, proc_time, index] for index, (enq_time, proc_time) in enumerate(tasks)]
        tasks.sort(reverse=True)
        # print("tasks", tasks)

        cur_time = tasks[-1][0]
        while tasks or min_heap:
            while tasks and tasks[-1][0] <= cur_time:
                task = tasks.pop()
                heapq.heappush(min_heap, [task[1], task[2]])

            if min_heap:
                proc_time, idx = heapq.heappop(min_heap)
                res.append(idx)
                cur_time += proc_time
            else:
                cur_time = tasks[-1][0]
        
        return res


