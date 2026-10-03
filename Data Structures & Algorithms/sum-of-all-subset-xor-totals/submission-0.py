class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.N = len(nums)
        self.res = 0

        def all_subsets(i, cur):
            if i >= self.N:
                self.res += cur
                return 
            
            all_subsets(i+1, cur)
            all_subsets(i+1, cur ^ nums[i])
        
        all_subsets(0, 0)
        return self.res

            


"""
010
101
110
"""