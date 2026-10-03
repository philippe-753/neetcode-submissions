class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        memo = {}

        def dfs(arr):

            if not arr:
                return 0
            
            if tuple(arr) in memo:
                return memo[tuple(arr)]
            
            res = 0
            for i, num in enumerate(arr):
                before = 1 if i == 0 else arr[i-1]
                after = 1 if i == len(arr) - 1 else arr[i + 1]
                res = max(res, before*num*after + dfs(arr[:i] + arr[i+1:]))
            
            memo[tuple(arr)] = res

            return res
        
        return dfs(nums)
            

             