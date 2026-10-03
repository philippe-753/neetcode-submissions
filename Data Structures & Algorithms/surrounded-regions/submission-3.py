class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])

        change = [[True] * C for _ in range(R)]

        def dfs(row, col):

            if not (0 <= row < R) or not (0 <= col < C):
                return None
            
            if row == R-1 and col == C-1:
                print("here")
            
            if not change[row][col] or board[row][col] == "X":
                return None


            change[row][col] = False
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(row+dr, col+dc)
             
        for col in range(C):
            if board[0][col] == "O":
                dfs(0, col)
            if board[R-1][col] == "O":
                dfs(R-1, col)
        
        for row in range(R):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][C-1] == "O":
                dfs(row, C-1)
                
        for row in range(R):
            for col in range(C):
                if change[row][col]:
                    board[row][col] = "X"
                else:
                    board[row][col] = "O"


        
