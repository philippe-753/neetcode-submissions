class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = r

        while l <= r:
            mid = (l + r) // 2

            if self.can_eat_piles(piles, mid, h):

                best = mid
                r = mid - 1
            else:

                l = mid + 1

        return best


    def can_eat_piles(self, piles, rate, h) -> bool:
        total_hours = sum(math.ceil(p / rate) for p in piles)
        return total_hours <= h