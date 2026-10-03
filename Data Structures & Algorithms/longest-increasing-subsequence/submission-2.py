class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N

        for i in range(N-1, -1, -1):
            for j in range(i+1, N):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)

                















        # def dfs(i:int, arr:list) -> None:
        #     nonlocal res

        #     if i == N:
        #         res = max(len(arr), res)
        #         return
            
        #     if arr and nums[i] > arr[-1]:
        #         # Take
        #         arr.append(nums[i])
        #         dfs(i+1, arr)
        #         arr.pop()
            
        #     elif not arr:
        #         # Take
        #         arr.append(nums[i])
        #         dfs(i+1, arr)
        #         arr.pop()

        #     # Don't rake
        #     dfs(i + 1, arr)
        
        # dfs(0, [])
        # return res

            
        

                