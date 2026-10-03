from collections import defaultdict
class Solution:
    def findOrder(self, N: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[pre].append(course)
        
        visit = [0] * N # 0 not visited, 1 visited, -1 cycle detexted
        res = []

        def dfs(node):
            if visit[node] == -1:
                return False
            
            if visit[node] == 1:
                return True

            visit[node] = -1            
            for course in adj[node]:
                if not dfs(course):
                    return False
            visit[node] = 1
            res.append(node)
            return True

        for i in range(N):
            if not dfs(i):
                return []

        return res[::-1]


        
