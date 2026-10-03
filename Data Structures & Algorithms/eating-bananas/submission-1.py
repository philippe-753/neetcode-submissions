class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return -1
        
        max_num_bananas = max(piles)

        def can_eat_all_bananas(banana_num):#
            cur_hours = 0
            for pile in piles:
                cur_hours += math.ceil(float(pile) / banana_num)
                if cur_hours > h:
                    return False
            return True if cur_hours <= h else False
        
        def binary_search(left, right):
            best = -1
            while left <= right:
                mid = (left + right) // 2
                if can_eat_all_bananas(mid):
                    best = mid
                    right = mid -1
                else:
                    left = mid + 1

            return best
        
        print(can_eat_all_bananas(25))
        return binary_search(1, max_num_bananas)
            

