from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        num_freq = Counter(nums)
        res = []

        def dfs(i, perm):

            if i == N:
                res.append(perm.copy())
                return
            
            for num, freq in num_freq.items():
                if freq <= 0:
                    continue
                perm.append(num)
                num_freq[num] -= 1
                dfs(i+1, perm)
                perm.pop()
                num_freq[num] += 1
        
        dfs(0, [])
        return res

