class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char:set() for word in words for char in word}

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            min_len = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""

            for j in range(min_len):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break
    
        memo = defaultdict(int) # -1 = cycle detected, 1 = visited.
        res = []

        def dfs(char):

            if memo[char] == -1:
                return False
            
            if memo[char] == 1:
                return True
            
            memo[char] = -1 # it will trigger if seen.
            for next_char in adj[char]:
                if not dfs(next_char):
                    return False
            memo[char] = 1
            res.append(char)
            return True

        for char in adj:
            if not dfs(char):
                return ""
        
        return "".join(res[::-1])













