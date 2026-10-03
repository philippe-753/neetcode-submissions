class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        picked = [False] * N

        def dfs(start, cur, picked):
            if start == N:
                res.append(cur.copy())
                return
            
            for i in range(0, N):
                if picked[i]:
                    continue

                picked[i] = True
                cur.append(nums[i])
                dfs(start + 1, cur, picked)
                cur.pop()
                picked[i] = False

        dfs(0, [], picked)
        return res




