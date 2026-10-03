class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        N = len(wordList)
        word_length = len(wordList[0])
        adj = defaultdict(list)
        for word1 in wordList:
            for word2 in wordList:
                if word1 == word2:
                    continue
                count_diff = 0
                for i in range(word_length):
                    if word1[i] != word2[i]:
                        count_diff += 1
                    if count_diff > 1:
                        break
                if count_diff == 1:
                    adj[word1].append(word2)

                
        print("adj:", adj)
        
        queue = deque([])
        visited = set()
        queue.append(beginWord)
        visited.add(beginWord)
        res = 1

        while queue:
            length = len(queue)
            print("----")
            for _ in range(length):
                node = queue.popleft()
                print("node:", node)
                
                if node == endWord:
                    return res

                for nei in adj[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)

            res += 1

        return 0
