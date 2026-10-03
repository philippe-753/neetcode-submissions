class Solution:
    def generateParenthesis(self, N: int) -> List[str]:
        res = []

        def dfs(open_ratio, total_open, cur):

            if total_open == N and len(cur) == 2*N:
                res.append("".join(cur))
                return
            
            if total_open < N:
                cur.append("(")
                dfs(open_ratio + 1, total_open + 1, cur)
                cur.pop()
            
            if open_ratio >= 1:
                cur.append(")")
                dfs(open_ratio - 1, total_open, cur)
                cur.pop()
        
        dfs(0, 0, [])
        return res
            

"""
                           ( 
            (                              )
    (               )                      (
                                                   
    )          (         )          (               )
    )          )         (          )               (
    )          )         )          )               )

N * N!
"""

