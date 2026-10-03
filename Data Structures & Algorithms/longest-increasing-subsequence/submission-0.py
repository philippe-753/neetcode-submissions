class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0


        def dfs(i:int, arr:list) -> None:
            nonlocal res

            if i == N:
                res = max(len(arr), res)
                return
            
            if arr and nums[i] > arr[-1]:
                # Take
                arr.append(nums[i])
                dfs(i+1, arr)
                arr.pop()
            
            elif not arr:
                # Take
                arr.append(nums[i])
                dfs(i+1, arr)
                arr.pop()

            # Don't rake
            dfs(i + 1, arr)
        
        dfs(0, [])
        return res

            
        

                