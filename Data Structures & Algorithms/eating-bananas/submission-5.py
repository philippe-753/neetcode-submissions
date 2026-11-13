import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = -1

        while l <= r:
            mid = (l + r) // 2

            if self.can_eat_all_bananas(piles, h, mid):
                best = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return best



    
    def can_eat_all_bananas(self, piles, h, rate) -> bool:
        return sum(math.ceil(pile/rate) for pile in piles) <= h