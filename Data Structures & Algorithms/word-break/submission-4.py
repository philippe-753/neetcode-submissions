class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        N = len(s)
        dp = [False] * (N + 1)
        dp[-1] = True

        for i in range(N, -1, -1):
            for word in word_dict:
                if dp[i] and i - len(word) >= 0 and s[i-len(word):i] == word:
                    dp[i-len(word)] = True
        
        return dp[0]
                









        # def dfs(i, cur):
            
        #     if len(cur) == N:
        #         return True
            
        #     for word in word_dict:
        #         if i + len(word) <= N and s[i:i+len(word)] == word:
        #             if dfs(i + len(word), cur + word):
        #                 return True
                
        #     return False
            
        # return dfs(0, "")               
                