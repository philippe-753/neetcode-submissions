class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return self.is_pal(l + 1, r, s) or self.is_pal(l, r -1, s)
            l, r = l + 1, r - 1
        
        return True
        

    def is_pal(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                    return False
            l += 1
            r -= 1
        return True

        return is_palindrome(0, len(s)-1, 1)
        

            