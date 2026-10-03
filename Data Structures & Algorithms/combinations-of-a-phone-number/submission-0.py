class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        N = len(digits)
        num_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        cur = []
        res = []

        def dfs(i):
            if i == N:
                res.append("".join(cur))
                return
            
            for char in num_to_char[digits[i]]:
                cur.append(char)
                dfs(i+1)
                cur.pop()
        dfs(0)
        return res