class Solution:
    def countComponents(self, N: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        

        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

        res = 0
        for node in range(N):
            if node not in visited:
                res += 1
                dfs(node)
        
        return res