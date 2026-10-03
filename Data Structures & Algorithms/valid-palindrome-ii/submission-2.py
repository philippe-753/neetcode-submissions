class Solution:
    def validPalindrome(self, s: str) -> bool:
        N = len(s)
        def is_palin(l, r):
            while l < r:
                while l < r and not s[l].isalnum():
                    l += 1
                while r > l and not s[r].isalnum():
                    r -= 1
                
                if s[l].lower() != s[r].lower():
                    return False, l, r
                l += 1
                r -= 1

            return True, l, r

        valid_palin, l, r = is_palin(0, N - 1)
        if valid_palin or is_palin(l+1, r)[0] or is_palin(l, r-1)[0]:
            return True
        
        return False

        



        

            