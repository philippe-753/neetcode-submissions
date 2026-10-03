class Solution:
    def validTree(self, N: int, edges: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = [0]* N # 1 == visited, -1 cycle detected.

        print("adj", adj)
        def dfs(node, par):
            if visited[node] != 0:
                return visited[node]
            
            visited[node] = -1
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node) == -1:
                    return False

            visited[node] = 1
            return True
        
        
        return dfs(0, -1) and all(node == 1 for node in visited)