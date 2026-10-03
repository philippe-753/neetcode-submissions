class Solution:
    def findMaximizedCapital(self, K: int, W: int, profits: List[int], capital: List[int]) -> int:
        N = len(capital)
        cap_to_pro = [[capital[i], profits[i]] for i in range(N)]
        cap_to_pro.sort()
        max_heap = []
        i, count = 0, 0

        while count < K:
            while i < N and cap_to_pro[i][0] <= W:
                heapq.heappush(max_heap, -cap_to_pro[i][1])
                i += 1
            # print("--------")
            # print("count:", count)
            # print("max_heap", max_heap)
            if not max_heap:
                break
            prof = -heapq.heappop(max_heap)
            W += prof
            count += 1
            # print("W:", W)

        return W

