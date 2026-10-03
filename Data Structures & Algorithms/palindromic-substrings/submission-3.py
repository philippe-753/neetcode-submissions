class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        self.res = 0

        def _is_palindrome(left, right):
            while right < N and left >= 0 and s[left] == s[right]:
                left -= 1
                right += 1
                self.res += 1
        
        
        for i in range(N):
            # odd
            left, right = i, i
            _is_palindrome(left, right)

            # even
            left, right = i, i + 1
            _is_palindrome(left, right)
        
        return self.res