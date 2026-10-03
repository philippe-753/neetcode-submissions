from collections import defaultdict
class Solution:
    def canFinish(self, N: int, prerequisites: List[List[int]]) -> bool:
        neighbours = defaultdict(list)
        for course, pre in prerequisites:
            neighbours[course].append(pre)

        visited = set()

        def dfs(node):
            if node in visited:
                return False

            visited.add(node)
            for nei in neighbours[node]:
                if not dfs(nei):
                    return False
            visited.remove(node)
            return True
        
        for i in range(N):
            if not dfs(i):
                return False
        
        return True




























# 
# 
        # graph = defaultdict(list)
        # for course, pre in prerequisites:
            # graph[course].append(pre)
# 
        # visited = set()
# 
# 
        # def dfs(course):
            # 
            # if course in visited:
                # return False
            # 
            # visited.add(course)
            # for pre in graph[course]:
                # if not dfs(pre):
                    # return False
            # visited.remove(course)
            # graph[course] = []
            # return True
        # 
        # for i in range(numCourses):
            # if not dfs(i):
                # return False
        # return True
        # 
        # 
# 
# 