class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1      

        left = 0
        right = 1
        char_seen = set(s[left])
        res = 0

        while right < len(s):
            if s[right] not in char_seen:
                char_seen.add(s[right])
                res = max(res, right - left + 1)
                right += 1
            else:
                while s[right] in char_seen:
                    char_seen.remove(s[left])
                    left += 1
        
        return res
            
            
            

            