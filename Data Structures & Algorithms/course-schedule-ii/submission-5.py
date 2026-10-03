class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visit = {} # False if visited, True = Cycle
        res = []

        def dfs(course):
            if course in visit: return visit[course]
            visit[course] = True
            for pre in graph[course]:
                if dfs(pre):
                    return True
            visit[course] = False
            res.append(course)
            return False
        

        for i in range(numCourses):
            if dfs(i):
                return []
        
        return res
            

        
