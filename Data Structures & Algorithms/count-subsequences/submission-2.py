class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(t) + 1) for _ in range(len(s) + 1)]
        
        for j in range(0, len(s) + 1):
            dp[j][0] = 1
        
        for i in range(1, len(t)+1):
            for j in range(1, len(s)+1):
                dp[j][i] = dp[j - 1][i]
                if s[j-1] == t[i-1]:
                    dp[j][i] += dp[j - 1][i - 1]

        return dp[len(s)][len(t)]




"""

      c  a  t
   
c  1  1  0  0  
a  1  1  1     
a  1  0  2
a  1  0  3  
t  1  0  0  3



"""
            
