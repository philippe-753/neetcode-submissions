from copy import deepcopy

class Solution:
    def __init__(self):
        self.res = []
        self.cur = []
        self.visited = set()

    def solveNQueens(self, N: int) -> List[List[str]]:
        self.R, self.C, self.N = N, N, N
        for col in range(self.R):
            self.dfs(0, col)
        
        final_answer = []
        print("self.res:", self.res)
        for solution in self.res:
            cur_sol = []
            for x_cor, y_cor in solution:
                cur_sol.append(self.coordinates_to_draw(y_cor))
            final_answer.append(cur_sol)
        
        return final_answer

    def in_used_diagonals(self, row, col) -> bool:
        for q_row, q_col in self.visited:
            if col == q_col or col == q_col + (row - q_row) or col == q_col - (row - q_row):
                return True
        return False

    def coordinates_to_draw(self, x_cor):
        return "."*x_cor + "Q" + "."*(self.N - x_cor - 1)

    def dfs(self, row:int, col:int):

        if row == self.N:
            # print("here", self.cur)
            self.res.append(deepcopy(self.cur))
            return None

        if not 0 <= row < self.R or not 0 <= col < self.C or (row, col) in self.visited:
            return None
        
        if self.in_used_diagonals(row, col):
            print("true!")
            return None

        # print("------")
        # print("row, col", row, col)
        # print("cur:", self.cur)
        
        self.visited.add((row, col))
        self.cur.append([row, col])

        if row == self.N - 1:
            self.res.append(deepcopy(self.cur))
        else:
            for n_c in range(self.N):
                self.dfs(row + 1, n_c)
        self.visited.remove((row, col))
        self.cur.pop()


        
        

            
    