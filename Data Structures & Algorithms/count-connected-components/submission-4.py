class Solution:
    def countComponents(self, N: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
    
        visit = set()

        def dfs(node, par):
            if node in visit:
                return
            visit.add(node)
            for nei in adj[node]:
                if nei == par or nei in visit:
                    continue
                dfs(nei, node)
        
        res = 0
        for node in range(N):
            if node not in visit:
                dfs(node, -1)
                res += 1
        
        return res
            
