from collections import defaultdict, deque
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        max_heap = []
        res = []
        for i in range(k):
            max_heap.append((-nums[i], i))

        heapq.heapify(max_heap)
        res.append(-max_heap[0][0])

        for i in range(k, N):
            heapq.heappush(max_heap, (-nums[i], i))

            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            
            res.append(-max_heap[0][0])

        return res
            




        # if k == 1:
        #     return nums
        # N = len(nums)
        # nums_freq = defaultdict(int)
        # left = 0
        # res = []
        # queue = deque([])

        # cur_max = -float("inf")
        # for i in range(k):
        #     cur_max = max(cur_max, num[i])
        #     queue.append(nums[i])
        
        # res.append(cur_max)
        # queue.pop()

        # for i in range(N):


        


[1, 2, 1, 0, -1, 8]