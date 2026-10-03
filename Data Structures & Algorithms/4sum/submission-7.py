from collections import Counter

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        res = []
        print("nums:", nums)

        for a, num in enumerate(nums):
            if a > 0 and nums[a-1] == num:
                continue

            b = a + 1
            print("------")
            print("a:", a)
            while b < N - 2:
                c, d = b + 1, N - 1
                if b > a + 1 and nums[b] == nums[b-1]:
                    b +=1
                    continue
            
                print("b", b)
                while c < d:
                    print("c, d", c, d)
                    cur_sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if cur_sum > target:
                        d -= 1
                    elif cur_sum < target:
                        c += 1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while nums[c] == nums[c-1] and c < d:
                            c += 1
                b += 1
        return res

                
      