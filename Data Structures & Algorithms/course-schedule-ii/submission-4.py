class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visit = {} # False if visited, True = Cycle
        res = []

        def dfs(course):
            if course in visit: return visit[course]
            visit[course] = False
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visit[course] = True
            res.append(course)
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res
            

        
