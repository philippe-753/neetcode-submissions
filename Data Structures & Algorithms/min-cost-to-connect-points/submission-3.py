from collections import defaultdict
import heapq

class DUS:
    def __init__(self, N):
        self.par = [i for i in range(N)]
        self.rank = [1 for i in range(N)]

    def union(self, node1, node2):
        par1, par2 = self.find(node1), self.find(node2)
        if par1 == par2:
            return False

        if self.rank[par1] >= self.rank[par2]:
            self.rank[par1] += self.rank[par2]
            self.par[par2] = par1
        else:
            self.rank[par2] += self.rank[par1]
            self.par[par1] = par2
        
        return True

    def find(self, node):
        while node != self.par[node]:
            node = self.par[self.par[node]]
        
        return node


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        dsu = DUS(N)

        dis = []
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points):
                if i == j or (x1, y1) == (x2, y2):
                    continue
                mah = abs(x1-x2) + abs(y1-y2)
                dis.append([mah, i, j])
        
       
        res = 0
        dis.sort()
        for cost, node1, node2 in dis:
            if dsu.union(node1, node2):
                res += cost 

        return res
        


