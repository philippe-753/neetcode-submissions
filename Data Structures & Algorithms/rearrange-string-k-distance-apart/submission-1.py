from collections import Counter, deque
import heapq

class Solution:
    def rearrangeString(self, s: str, K: int) -> str:
        char_freq = Counter(s)
        N, M = len(s), len(char_freq) # N = len of s, M len of unique chars (upto 26)
        print("char_freq", char_freq)
        res = ""
        min_heap = [[-freq, char] for char, freq in char_freq.items()]
        heapq.heapify(min_heap)
        queue = deque([])

        for i in range(N):
            # print("-------")
            # print("i:", i)
            # print("min_heap:", min_heap)
            # print("queue", queue)
            while queue and i - queue[0][0] >= K:
                _, freq, char = queue.popleft()
                heapq.heappush(min_heap, [freq, char])

            if not min_heap:
                return ""

            freq, char = heapq.heappop(min_heap)
            res += char
            freq += 1
            
            if freq < 0:
                queue.append([i, freq, char])
            
            # print("res:", res)

        return res



