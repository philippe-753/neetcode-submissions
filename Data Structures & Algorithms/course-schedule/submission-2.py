class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)

        visited = set()


        def dfs(course):
            
            if course in visited:
                return False
            
            visited.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            graph[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        

