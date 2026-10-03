from collections import defaultdict
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        num_freq = set()  
        for num in nums:
            if num in num_freq:
                return num
            num_freq.add(num)

        return -1
            
        