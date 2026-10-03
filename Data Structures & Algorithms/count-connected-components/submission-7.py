class Solution:
    def countComponents(self, N: int, edges: List[List[int]]) -> int:
        par = [i for i in range(N)]
        rank = [1 for _ in range(N)]

        def union(node1, node2):
            # Unites two nodes together
            par1, par2 = find(node1), find(node2)

            if par1 == par2:
                return False

            if rank[par1] >= rank[par2]:
                par[par2] = par1
                rank[par1] += rank[par2]
            else:
                par[par1] = par2
                rank[par2] += rank[par1]
            
            return True

        

        def find(node):
            # finds the parents.
            while node != par[node]:
                par[node] = par[par[node]] # small optimisastion
                node = par[node]

            return node

        res = N
        for v, e in edges:
            if union(v, e):
                res -= 1

        return res
        


