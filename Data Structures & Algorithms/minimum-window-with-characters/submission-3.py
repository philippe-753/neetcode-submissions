from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
            
        t_freq = Counter(t)
        cur_freq = defaultdict(int)

        N = len(s)
        t_len = len(t)

        left = 0
        right = 0
        best_left, best_right, best_len = left, N-1, float("inf")
        count = 0

        for right in range(N):
            char = s[right]
            if cur_freq[char] < t_freq[char]:
                count += 1
            cur_freq[char] += 1

            while count == t_len and left <= right:
                best_len = min(best_len, right-left+1)
                if right - left < best_right - best_left:
                    best_left, best_right = left, right

                cur_freq[s[left]] -= 1
                if cur_freq[s[left]] < t_freq[s[left]]:
                    count -= 1
                left += 1
        
        return s[best_left:best_right+1] if best_len != float("inf") else ""


