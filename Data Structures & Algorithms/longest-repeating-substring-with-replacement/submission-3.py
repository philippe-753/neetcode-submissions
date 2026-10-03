class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        left = 0
        res = 0
        max_freq = 0

        for right, char in enumerate(s):
            char_freq[char] += 1
            max_freq = max(max_freq, char_freq[char])
            diff = right - left + 1 - max_freq
            while diff > k:
                char_freq[s[left]] -= 1
                left += 1
                diff = right - left + 1 - max_freq
                
            res = max(res, right - left + 1)

        return res


