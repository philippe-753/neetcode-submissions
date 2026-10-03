class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        self.res = []

        def dfs(i, arr, cur_sum):
            if cur_sum == target:
                self.res.append(arr.copy())
                return
            if i >= N or cur_sum > target:
                return
            
            arr.append(nums[i])
            dfs(i, arr, cur_sum + nums[i])
            arr.pop()
            dfs(i + 1, arr, cur_sum)
        
        dfs(0, [], 0)
        return self.res
            
            