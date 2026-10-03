class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        N = len(people)
        people.sort()
        left = 0
        right = N -1
        res = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            res += 1
        
        return res