class DUS:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [1 for _ in range(N)]

    def union(self, node1:int, node2:int) -> bool:
        """ Unites two nodes together. 
        Args:
                node1: int = First node
                node2: int = Second node.

        Returns:
            bool: True if node1 and node2 do not share the same parerent
            and have been linked together, False otherwise.
        """
        p1, p2 = self.find(node1), self.find(node2)

        if p1 == p2:
            return False 

        if self.rank[p1] >= self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        
        return True


    def find(self, node:int) -> int:
        # find (most) parent of a node.
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]

        return node

class Solution:
    def countComponents(self, N: int, edges: List[List[int]]) -> int:
       
        dus = DUS(N)
        res = N
        for v, e in edges:
            if dus.union(v, e):
                res -= 1

        return res
        


