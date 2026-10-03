class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[pre].append(course)
        
        visit = {} # False if visited, True = Cycle
        res = []

        def dfs(pre):
            if pre in visit: return visit[pre]
            visit[pre] = True
            for course in adj[pre]:
                if dfs(course):
                    return True
            visit[pre] = False
            res.append(pre)
            return False
        

        for i in range(numCourses):
            if dfs(i):
                return []
        
        return res[::-1]
            

        
