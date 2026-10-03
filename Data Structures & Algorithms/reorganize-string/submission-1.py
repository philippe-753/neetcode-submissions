from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        
        # O(n!) solution:


        # O(N log N)
        N = len(s)
        i = 0
        char_freq = Counter(s)
        # print("char_freq:", char_freq)
        max_heap = [[-freq, char] for char, freq in char_freq.items()]
        heapq.heapify(max_heap)
        res = ""
        prev = ""
        # print("max_heap:", max_heap)
        while i < N:
            # print("-------")
            # print("i:", i)
            
            freq, char = heapq.heappop(max_heap)
            # print("char, freq:", char, -freq)
            if char == prev:
                if not max_heap or -max_heap[0][0] <= 0:
                    return ""
                
                freq2, char2 = heapq.heappop(max_heap)
                heapq.heappush(max_heap, [freq, char])
                freq, char = freq2, char2
            
            res += char
            if -(freq - 1) > 0:
                heapq.heappush(max_heap, [(freq + 1), char])
            
            # Update
            prev = char
            i += 1
        
        return res
        




            


        