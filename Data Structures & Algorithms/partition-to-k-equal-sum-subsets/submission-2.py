class Solution:
    def canPartitionKSubsets(self, nums: List[int], K: int) -> bool:
        N = len(nums)
        if sum(nums) % K != 0:
            return False
        
        tar_sum = sum(nums) // K
        nums.sort(reverse=True)

        print("tar_sum", tar_sum)
        print("nums:", nums)
        used = [False] * N
        
        def dfs(i, k, cur):
            if k == 0:
                return True
                
            if cur == tar_sum:
                return dfs(0, k-1, 0)
        
            for idx in range(i, N):
                if used[idx] or cur + nums[idx] > tar_sum:
                    continue

                used[idx] = True
                if dfs(idx+1, k, cur + nums[idx]):
                    return True
                used[idx] = False

            return False

        return dfs(0, K, 0)
