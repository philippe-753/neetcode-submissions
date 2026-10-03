from collections import Counter

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        num_freq = Counter(nums)
        nums.sort()
        res = set()
        for i in range(N):
            num1 = nums[i]
            num_freq[num1] -= 1
            for j in range(i+1, N):
                num2 = nums[j]
                num_freq[num2] -= 1
                for k in range(j+1, N):
                    num3 = nums[k]
                    num_freq[num3] -= 1
                    cur_tar = target - (num1 + num2 + num3)
                    if cur_tar in num_freq and num_freq[cur_tar] > 0:
                        cur = [num1, num2, num3, cur_tar]
                        cur.sort()
                        res.add(tuple(cur))                  
                    num_freq[num3] += 1
                num_freq[num2] += 1
        return list(res)
