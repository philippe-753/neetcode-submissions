class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        total = sum(nums)
        target = int(total / 2)
        if total % 2 == 1:
            return False

        def dfs(i, cur):

            if i == N or cur > int(total/2):
                return False

            if cur == int(total/2):
                return True
            
            take = dfs(i+1, cur + nums[i])
            dont_take = dfs(i+1, cur)
            return take or dont_take
        

        return dfs(0, 0)
