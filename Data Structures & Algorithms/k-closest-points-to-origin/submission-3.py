import heapq
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Time: O(N long N) Space: O(N) - > O(N lon K ), Space: O(K)
        points.sort(key= lambda p: (p[0]**2 + p[1]**2))
        return points[:k]
