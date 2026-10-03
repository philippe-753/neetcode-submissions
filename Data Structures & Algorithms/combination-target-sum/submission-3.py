class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        self.res = []
        self.visited = set()

        def dfs(idx, arr, cur_sum):
            if cur_sum == target and tuple(arr) not in self.visited:
                self.visited.add(tuple(arr))
                return self.res.append(arr)
            if idx >= N or cur_sum > target: return None
            
            dfs(idx+1, arr, cur_sum)
            dfs(idx, arr + [nums[idx]], cur_sum + nums[idx])
        
        dfs(0, [], 0)
        return self.res
            
            