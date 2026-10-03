class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        cur, res = [], []

        def dfs(i):
            if i == N: 
                res.append(cur.copy())
                return
            
            # Take
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()

            # Don't take
            dfs(i+1)
        
        dfs(0)
        return res

