class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def dfs(row, col, i, visited):
            
            if i >= len(word):
                return True
            
            visited.add((row, col))
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited and board[nr][nc] == word[i]:
                    if dfs(nr, nc, i + 1, visited):
                        return True
            visited.remove((row, col))
            return False
        
        for row in range(R):
            for col in range(C):
                if board[row][col] == word[0]:
                    if dfs(row, col, 1, set()):
                        return True

        return False