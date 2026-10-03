class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C, N = len(board), len(board[0]), len(word)


        def dfs(row:int, col:int, i:int) -> bool:

            if i == N:
                return True

            if not 0 <= row < R or not 0 <= col < C or board[row][col] == "-1":
                return False
            
            if word[i] != board[row][col]:
                return False
            
            
            board[row][col] = "-1"
            
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = row + dr, col + dc
                if dfs(nr, nc, i+1):
                    return True
            
            board[row][col] = word[i]
            
            return False
        
        for row in range(R):
            for col in range(C):
                if board[row][col] == word[0] and dfs(row, col, 0):
                    return True
        
        return False
        
        