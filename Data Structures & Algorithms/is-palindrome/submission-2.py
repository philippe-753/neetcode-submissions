class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            l_char = s[left].lower()
            r_char = s[right].lower()
            
            while left < right and not l_char.isalnum():
                left += 1
                l_char = s[left].lower()
            

            while left < right and not r_char.isalnum():
                right -= 1
                r_char = s[right].lower()

            if l_char != r_char:
                return False
            
            left += 1
            right -= 1
        
        return True
                
            
            
            
