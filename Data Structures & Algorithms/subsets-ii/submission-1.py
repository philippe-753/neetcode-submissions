class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        nums.sort()
        visited = set()

        def dfs(i, sub):
            if i == N:
                if tuple(sub) not in visited:
                    res.append(sub.copy())
                    visited.add(tuple(sub))
                return
            sub.append(nums[i])
            dfs(i+1, sub)
            sub.pop()
            
            while i + 1 < N and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, sub)

        dfs(0, [])
        return res