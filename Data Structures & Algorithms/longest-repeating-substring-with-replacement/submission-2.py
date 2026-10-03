class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        left = 0
        res = 0

        def get_max_freq(char_freq):
            max_freq = 0
            for char, freq in char_freq.items():
                max_freq = max(max_freq, freq)
            return max_freq

        for right, char in enumerate(s):
            # print("----")
            # print("right, char:", right, char)
            char_freq[char] += 1
            max_freq = get_max_freq(char_freq)
            diff = right - left + 1 - max_freq
            while diff > k:
                char_freq[s[left]] -= 1
                left += 1
                diff = right - left + 1 - max_freq
                
            res = max(res, right - left + 1)

        return res


