class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        visited = set()
        N = len(nums)

        def backtrack(i, arr, cur_sum):
            
            if i == N or cur_sum > target:
                return None
            
            if cur_sum == target:
                if tuple(arr) not in visited:
                    res.append(arr)
                    visited.add(tuple(arr))
                return None

            # dont take
            backtrack(i+1, arr, cur_sum)

            # take and move forward
            backtrack(i+1, arr + [nums[i]], cur_sum + nums[i])

            # take but stay
            backtrack(i, arr + [nums[i]], cur_sum + nums[i])

        backtrack(0, [], 0)
        return res