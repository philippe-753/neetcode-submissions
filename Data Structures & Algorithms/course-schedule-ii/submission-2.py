class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visited = set()
        course_taken = set()
        res = []

        def add_course(course):
            if course not in course_taken:
                course_taken.add(course)
                res.append(course)

        def dfs(course):

            if course in visited:
                return False
            
            if graph[course] == []:
                add_course(course)
                return True

            visited.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False

            add_course(course)
            visited.remove(course)
            graph[course] = []

            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res
            

        
