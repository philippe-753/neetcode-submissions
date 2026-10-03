class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        N = len(matchsticks)
        res = []
        if sum(matchsticks) % 4 != 0:
            return False 

        matchsticks.sort(reverse=True)

        tar_len = sum(matchsticks) // 4
        sides = [0] * 4

        def dfs(i):
            if i == N:
                if all(side == tar_len for side in sides):
                    return True
                else:
                    return False
                
            for idx in range(4):
                if sides[idx] + matchsticks[i] <= tar_len:
                    sides[idx] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[idx] -= matchsticks[i]

            return False

        return dfs(0)
            


        
