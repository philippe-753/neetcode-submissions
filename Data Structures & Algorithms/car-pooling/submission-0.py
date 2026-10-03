class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        N = len(trips)
        i = 0

        while i < N:
            cap, start, to = trips[i] 
            while i + 1 < N and trips[i+1][1] < to:
                i += 1
                if cap + trips[i][0] > capacity:
                    return False

                cap += trips[i][0]
                
            i += 1
            
        return True


