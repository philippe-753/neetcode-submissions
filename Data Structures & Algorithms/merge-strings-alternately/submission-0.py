class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for char1, char2 in zip(word1, word2):
            res += char1 + char2
        
        if len(word1) > len(word2):
            res += word1[len(word2):]
        if len(word2) > len(word1):
            res += word2[len(word1):]
        
        return res
