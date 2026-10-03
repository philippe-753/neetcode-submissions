class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * (N + 1)
        dp[-1] = True
       
        
        for i in range(N-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= N and w == s[i:i+len(w)]:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]
                