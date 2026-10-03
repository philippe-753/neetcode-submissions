class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char:set() for word in words for char in word}
        print("adj:", adj)

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
        
        print("adj:", adj)

        visit, cycle = set(), set()
        res = []

        def dfs(char):

            if char in cycle:
                return True
            
            if char in visit:
                return False
            
            cycle.add(char) # it will trigger if seen.
            for next_char in adj[char]:
                if dfs(next_char):
                    return True
            cycle.remove(char)
            visit.add(char)
            res.append(char)


        for char in adj:
            if dfs(char):
                return ""
        
        return "".join(res[::-1])













