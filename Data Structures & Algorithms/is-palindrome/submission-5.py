class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alph = ""
        for char in s:
            if char.isalnum():
                s_alph += char

        l, r = 0, len(s_alph) - 1
        while l < r and s_alph[l].lower() == s_alph[r].lower():
            l += 1
            r -= 1
        if l >= r:
            return True
        
        return False
     
        

       
            
            
