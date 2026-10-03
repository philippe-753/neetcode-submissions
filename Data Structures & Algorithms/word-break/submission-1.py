class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # O(S*W**S)
        N = len(s)
        visited = [False] * N

        def dfs(i):

            if i == N:
                return True
            
            if visited[i]:
                return False
            
            visited[i] = True
            for word in wordDict:
                if i + len(word) <= N and word == s[i:i+len(word)]:
                    if dfs(i + len(word)):
                        return True
            
            return False

        return dfs(0)
