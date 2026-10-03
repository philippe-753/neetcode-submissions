class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        res = []
        visited = set()

        candidates.sort()
        def dfs(i, arr, cur_sum):
            if cur_sum == target and tuple(arr) not in visited:
                res.append(arr.copy())
                visited.add(tuple(arr))
                return
            if i >= N or cur_sum > target:
                return

            arr.append(candidates[i])
            dfs(i+1, arr, cur_sum + candidates[i])
            arr.pop()
            dfs(i+1, arr, cur_sum)

        dfs(0, [], 0)
        return res