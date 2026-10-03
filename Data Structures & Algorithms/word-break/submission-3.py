class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * (N + 1)
        dp[0] = True
       
        
        for i in range(N):
            for w in wordDict:
                if dp[i] and i + len(w) <= N and w == s[i:i+len(w)]:
                    dp[i+len(w)] = True
                    
        return dp[-1]
                