class Solution:
    def validTree(self, N: int, edges: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visit = [0] * N  # 1 = visited, -1 = cycle detected

        def dfs(node, par):
            if visit[node] == -1:
                return False
            if visit[node] == 1:
                return True
            
            visit[node] = -1
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False

            visit[node] = 1
            return True

        return dfs(0, -1) and all(v != 0 for v in visit)