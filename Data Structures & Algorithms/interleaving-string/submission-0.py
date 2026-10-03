class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}

        def dfs(i, j, k):
            print("------")
            print("i:", i)
            print("j:", j)
            print("k:", k)
            if k == len(s3) and i == len(s1) and j == len(s2):
                return True
            if k == len(s3):
                return False
            
            if (i, j, k) in memo:
                return memo[(i, j, k)]
            
            memo[(i, j, k)] = False
            if  i != len(s1) and s1[i] == s3[k]:
                if dfs(i + 1, j, k + 1):
                    memo[(i, j, k)] = True
            if j != len(s2) and s2[j] == s3[k]:
                if dfs(i, j + 1, k + 1):
                    memo[(i, j, k)] = True
            
            return memo[(i, j, k)]
        
        return dfs(0, 0, 0)


            