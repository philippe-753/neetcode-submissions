class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        res = 0

        def _is_palindrome(sub):
            left, right = 0, len(sub)-1
            while left <= right and sub[left] == sub[right]:
                left += 1
                right -= 1
            
            return left > right
        
        
        for i in range(N):
            for j in range(i+1, N+1):
                sub = s[i:j]
                if _is_palindrome(sub):
                    res += 1
        
        return res