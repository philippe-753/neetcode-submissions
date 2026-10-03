class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        word_dict = set(wordDict)
        cur, res = [], []

        def dfs(i, sub):
            if i == N:
                if sum([len(sub_word) for sub_word in cur]) == N:
                    res.append(" ".join(cur))
                return
            
            sub += s[i]
            if sub in word_dict:
                cur.append(sub)
                dfs(i+1, "")
                cur.pop()

            dfs(i+1, sub)
        
        dfs(0, "")
        return res
