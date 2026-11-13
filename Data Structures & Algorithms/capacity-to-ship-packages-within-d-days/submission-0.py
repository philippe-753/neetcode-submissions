class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        best = 0

        while l <= r:
            mid = (l + r) // 2
            if self.fits_capacity(weights, days, mid):
                best = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return best

        


    def fits_capacity(self, weights, days, cap) -> bool:
        cur_cap = cap
        for wei in weights:
            cur_cap -= wei
            if cur_cap < 0:
                days -= 1
                cur_cap = cap - wei 
        
        return days >= 1
