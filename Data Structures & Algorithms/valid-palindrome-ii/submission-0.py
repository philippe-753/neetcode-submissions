class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_palindrome(l, r, tries):
            while l < r:
                if s[l] != s[r]:
                    if tries < 1:
                        return False
                    return is_palindrome(l+1, r, tries - 1) or is_palindrome(l, r-1, tries - 1)
                else:
                    l += 1
                    r -= 1
            return True

        return is_palindrome(0, len(s)-1, 1)
        

            