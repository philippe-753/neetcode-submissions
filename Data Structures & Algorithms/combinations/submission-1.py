class Solution:
    def combine(self, N: int, K: int) -> List[List[int]]:
        res = []

        def dfs(start, cur):
            if len(cur) == K:
                res.append(cur.copy())
                return
        
            for i in range(start, N+1):
                cur.append(i)
                dfs(i + 1, cur)
                cur.pop()
            
        
        dfs(1, [])
        return res