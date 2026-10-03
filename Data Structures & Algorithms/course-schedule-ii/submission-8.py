from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, N: int, prerequisites: List[List[int]]) -> List[int]:
        
        pre_re = defaultdict(list)
        for course, pre in prerequisites:
            pre_re[course].append(pre)

        visited = set()
        visiting = set()
        res = []

        print("pre_re:", pre_re)

        def dfs(node):
            
            if node in visiting:
               return False
            if node in visited:
                return True

            visiting.add(node)  
            for nei in pre_re[node]:
                if not dfs(nei):
                    return False

            visiting.remove(node)
            visited.add(node)
            res.append(node)

            return True
        
        for i in range(N):
            if not dfs(i):
                return []

        return res
