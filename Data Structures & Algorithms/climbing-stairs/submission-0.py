class Solution:
    def climbStairs(self, N: int) -> int:
        if N <= 2:
            return N
            
        two_step = 1
        one_step = 2

        for i in range(2, N):
            cur = one_step + two_step
            two_step, one_step = one_step, cur
        
        return cur
