class Solution:
    def canFinish(self, N: int, prerequisites: List[List[int]]) -> bool:
        pre_re = defaultdict(list)
        for a, b in prerequisites:
            pre_re[b].append(a)
  
        visited = set()
        def dfs(node):
            if node in visited:
                return True
            
              
            visited.add(node)
            for nei in pre_re[node]:
                if nei in visited or not dfs(nei):
                    return False
                
            visited.remove(node)
            return True
        
        for i in range(N):
            if not dfs(i):
                return False

        return True

