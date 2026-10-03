class Solution:
    def totalNQueens(self, N: int) -> int:
        cols, pos_cols, neg_cols = set(), set(), set()
        res = 0
        
        def dfs(row):
            nonlocal res

            if row == N:
                res += 1
                return
            
            for col in range(N):
                if col in cols or (row + col) in pos_cols or (row - col) in neg_cols:
                    continue

                cols.add(col)
                pos_cols.add(row + col)
                neg_cols.add(row - col)

                dfs(row+1)

                cols.remove(col)
                pos_cols.remove(row + col)
                neg_cols.remove(row - col)

        dfs(0)
        return res
