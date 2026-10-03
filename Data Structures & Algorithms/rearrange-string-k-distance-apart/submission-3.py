from collections import Counter, deque
import heapq

class Solution:
    def rearrangeString(self, s: str, K: int) -> str:
        char_freq = Counter(s)
        N, M = len(s), len(char_freq) # N = len of s, M len of unique chars (upto 26)
        res = ""
        pq = [[-freq, char] for char, freq in char_freq.items()]
        heapq.heapify(pq)
        queue = deque([])

        for i in range(N):
            while queue and i - queue[0][0] >= K:
                _, freq, char = queue.popleft()
                heapq.heappush(pq, [freq, char])

            if not pq:
                return ""

            freq, char = heapq.heappop(pq)
            res += char
            freq += 1
            
            if freq < 0:
                queue.append([i, freq, char])

        return res



