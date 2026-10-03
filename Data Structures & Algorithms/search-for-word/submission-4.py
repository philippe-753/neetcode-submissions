class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def dfs(row, col, i):
        
            if i == len(word):
                return True
            
            if not 0 <= row < R or not 0 <= col < C or board[row][col] == "#" or board[row][col] != word[i]:
                return False
            
            board[row][col] = "#"
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = row + dr, col + dc
                if dfs(nr, nc, i+1):
                    return True
            board[row][col] = word[i]

            return False
        
        for row in range(R):
            for col in range(C):
                if dfs(row, col, 0):
                    return True
        return False
        
        