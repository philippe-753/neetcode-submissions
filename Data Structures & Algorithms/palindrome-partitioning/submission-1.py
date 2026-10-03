class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.res = []
        self.cur = []

        self._dfs(0)
        return self.res


    def _dfs(self, i):
        if i == len(self.s):
            if all(self._is_palindrome(sub) for sub in self.cur):
                self.res.append(self.cur.copy())
            return

        # get substrings
        for j in range(i+1, len(self.s)+1):
            self.cur.append(self.s[i:j])
            self._dfs(j)
            self.cur.pop()

    @staticmethod
    def _is_palindrome(sub):
        left, right = 0, len(sub) - 1
        while left <= right and sub[left] == sub[right]:
            left += 1
            right -= 1

        return left >= right
        

            
            

            


