class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        N = len(nums)
        memo = [-1] * target
        res = 0

        def dfs(total):
            nonlocal res

            if total > target:
                return 0
            
            if total == target:
                return 1

            if memo[total] != -1:
                return memo[total]

            count = 0
            for num in nums:
                count += dfs(total + num)
            
            memo[total] = count
            return memo[total]
        
        return dfs(0)




