import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = [[-a, "a"], [-b, "b"], [-c, "c"]]
        heapq.heapify(max_heap)
        res = ""

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            if freq >= 0:
                return res
            if len(res) >= 2 and res[-2:] == f"{char}{char}":
                if not max_heap or max_heap[0][0] >= 0:
                    return res
                freq2, char2 = heapq.heappop(max_heap)
                heapq.heappush(max_heap, [freq, char])
                freq, char = freq2, char2
            
            
            res += char
            freq += 1
            if freq < 0:
                heapq.heappush(max_heap, [freq, char])
        
        return res
            

                



