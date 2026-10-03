from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # return reversing the string, if cycle detected or lenth of res != N, return ""
        chars = set()
        for word in words:
            for char in word:
                chars.add(char)
        
        N = len(chars)
        res = ""

        # 1. we need to create directed relation ship A ->B C-> D.
        adj = defaultdict(set)
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            j = 0
            min_len = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:min_len]== word2[:min_len]:
                return ""

            while j < min(len(word1), len(word2)):
                if word1[j] == word2[j]:
                    j += 1
                else:
                    adj[word1[j]].add(word2[j])
                    break
        # There is cycle, and to add all the nodes in a post order fashio (i.e. last first)
        visited = [0] * N # visiting 2, visited 3
        char_to_idx = {char:i for i, char in enumerate(chars)}

        def dfs(node):
            nonlocal res
            
            node_idx = char_to_idx[node]
            if visited[node_idx] != 0:
                return visited[node_idx]

            visited[node_idx] = 2
            for nei in adj[node]:
                if dfs(nei) == 2:
                    print("cycle detected!")
                    return False # cycle detect
            
            res += node
            visited[node_idx] = 3
            return True



        for char in chars:
            if not dfs(char):
                return ""
        return res[::-1] if len(res) == N else ""




