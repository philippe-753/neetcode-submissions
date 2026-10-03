class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        M = sum([abs(num) for num in nums])
        cache = [[-1] * (M+1) for _ in range(N+1)]
        cache_neg = [[-1] * (M+1) for _ in range(N+1)]

        def dfs(i, cur):
            if i == N and cur == target:
                return 1
            if i == N and cur != target:
                return 0     
            if cur >=0 and cache[i][cur] != -1:
                return cache[i][cur]

            if cur <0 and cache_neg[i][-cur] != -1:
                return cache_neg[i][-cur]
            
            res = dfs(i+1, cur + nums[i]) + dfs(i+1, cur - nums[i])
            if cur >= 0:
                cache[i][cur] = res
            else:
                cache_neg[i][cur] = res

            return res
        
        return dfs(0, 0)
