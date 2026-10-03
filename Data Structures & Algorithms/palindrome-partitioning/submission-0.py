class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        res = []
        subs = []

        def is_palindrome(sub:str, left:int, right:int) -> bool:
            while left <= right:
                if sub[left] != sub[right]:
                    return False
                right -= 1
                left += 1
            return True


        def dfs(i):
            if i == N:
                res.append(subs.copy())
                return
            
            for j in range(i+1, N+1):
                sub = s[i:j]
                if is_palindrome(sub, 0, len(sub) - 1):
                    subs.append(sub)
                    dfs(j)
                    subs.pop()
            
        dfs(0)
        return res

            


