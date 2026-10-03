class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        def compute_palindrome(left, right):
            max_pal = 0
            max_left, max_right = left, right
            while left >= 0 and right < N and s[left] == s[right]:
                max_pal = right - left + 1
                max_left, max_right = left, right
                left -= 1
                right += 1
            
            return [max_pal, max_left, max_right]

        max_len = 0
        max_left, max_right = 0, 0
        for i in range(N):
            even, even_max_left, even_max_right = compute_palindrome(i, i+1)
            odd, odd_max_left, odd_max_right = compute_palindrome(i, i)
            
            if even > max_len:
                max_left, max_right = even_max_left, even_max_right
                max_len = even
                
            if odd > max_len:
                max_left, max_right = odd_max_left, odd_max_right
                max_len = odd
    
        return s[max_left:max_right+1]