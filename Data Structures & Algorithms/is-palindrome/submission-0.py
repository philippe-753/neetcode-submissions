class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        final_s = "" 
        for char in s:
            if char.isalnum():
                final_s += char

        
        return final_s == final_s[::-1]