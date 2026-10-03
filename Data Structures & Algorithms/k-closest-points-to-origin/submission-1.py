import heapq
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Time: O(N long N) Space: O(N) - > O(N lon K ), Space: O(K)
        dis_to_coor = defaultdict(list)
        for x, y in points:
            dis = x**2 + y**2
            dis_to_coor[dis].append([x, y])
            
        print("dis_to_coor:", dis_to_coor)
        keys = sorted(dis_to_coor)
        print("keys:", keys)
        res = []
        i = 0
        while len(res) != k:
            print(" dis_to_coor[keys[i]]:",  dis_to_coor[keys[i]])
            for coor in dis_to_coor[keys[i]]:
                print("coor:", coor)
                if len(res) < k:
                    res.append(coor)
            i += 1

        return res
