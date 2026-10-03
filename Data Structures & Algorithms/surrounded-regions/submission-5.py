class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])

        def dfs(row, col):

            board[row][col] = "V"

            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = dr + row, dc + col
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == "O":
                    dfs(nr, nc)

        for row in range(R):
            if board[row][0] == "O":
                dfs(row, 0)

            if board[row][C-1] == "O":
                dfs(row, C-1)

        for col in range(C):
            if board[0][col] == "O":
                dfs(0, col)

            if board[R-1][col] == "O":
                dfs(R-1, col)

        for row in range(R):
            for col in range(C):
                if board[row][col] == "V":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"
