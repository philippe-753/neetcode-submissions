class Solution:
    def generateParenthesis(self, N: int) -> List[str]:
        res = []
        cur = []

        def dfs(open_num, open_ratio):

            if open_num == N and open_ratio == 0:
                res.append("".join(cur))
                return

            if open_num < N:
                cur.append("(")
                dfs(open_num+1, open_ratio + 1)                
                cur.pop()
            
            if open_ratio > 0:
                cur.append(")")
                dfs(open_num, open_ratio - 1)
                cur.pop()
            
        dfs(0, 0)
        return res