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
            dfs(i+1, sub)

        dfs(0, [])
        return res