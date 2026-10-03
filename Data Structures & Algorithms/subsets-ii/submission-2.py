class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        cur, res = [], []
        nums.sort()

        def dfs(i):
            if i >= N:
                res.append(cur.copy())
                return 
                
            # Take
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()

            # Don't take
            while i + 1 < N and nums[i] == nums[i + 1]:
                i += 1

            dfs(i+1)
        
        dfs(0)
        return res
