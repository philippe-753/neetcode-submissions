class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = Counter(s1)
        s1_len = sum([freq for char, freq in s1_freq.items()])
        
        count = 0
        left = 0
        s2_freq = defaultdict(int)
        count = 0
        for char in s2:
            s2_freq[char] += 1
            count += 1
            while s2_freq[char] > s1_freq[char]:
                s2_freq[s2[left]] -= 1
                left += 1
                count -= 1
            if count == s1_len:
                return True
        
        return False
