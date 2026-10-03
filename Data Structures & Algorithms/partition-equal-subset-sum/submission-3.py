class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        total = sum(nums)
        target = int(total / 2)

        memo = [[-1] * (target+1) for _ in range(N + 1)]

        if total % 2 == 1:
            return False

        def dfs(i, cur):

            if i == N or cur > int(total/2):
                return False

            if cur == int(total/2):
                return True

            if memo[i][cur] != -1:
                return memo[i][cur]
            
            take = dfs(i+1, cur + nums[i])
            dont_take = dfs(i+1, cur)

            memo[i][cur] = take or dont_take
            return memo[i][cur]
        
        return dfs(0, 0)