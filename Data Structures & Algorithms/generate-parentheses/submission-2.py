class Solution:
    def generateParenthesis(self, N: int) -> List[str]:
        res = []
        cur = []

        def dfs(n_open, rat):
            if n_open == N and rat == 0:
               res.append("".join(cur))
               return

            # Open a parentheses
            if n_open < N:
                cur.append("(")
                dfs(n_open + 1, rat + 1)
                cur.pop()

            # close a parentheses
            if rat > 0:
                cur.append(")")
                dfs(n_open, rat - 1) 
                cur.pop()

        dfs(0, 0)
        return res


