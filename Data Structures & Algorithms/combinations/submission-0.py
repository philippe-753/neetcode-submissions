class Solution:
    def combine(self, N: int, K: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            nonlocal res

            if total == K:
                res.append(cur.copy())
                return

            if i > N: 
                return
        
            # Include
            cur.append(i)
            dfs(i + 1, cur, total+1)
            cur.pop()
            # Do not include
            dfs(i + 1, cur, total)
        
        dfs(1, [], 0)
        return res