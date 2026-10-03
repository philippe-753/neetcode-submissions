from collections import defaultdict, Counter, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        word_len = len(beginWord)
        wordList.append(beginWord)
        N = len(wordList)
        
        word_map = defaultdict(list)
        
        for word1 in wordList:
            word1_freq = Counter(word1)
            print("word1_freq:", word1_freq)
            for word2 in wordList:
                if word1 == word2:
                    continue
                count_diff = 0
                for i in range(word_len):
                    if word1[i] != word2[i]:
                        count_diff += 1
                    if count_diff > 1:
                        break
                if count_diff == 1:
                    word_map[word1].append(word2)
                    # word_map[word2].append(word1)
                    
        visited = set()
        queue = deque([]) #current word,  number of word changes, 
        queue.append([beginWord, 1])
        visited.add(beginWord)
        
        res = float("inf")

        while queue:
            node, time = queue.popleft()

            if node == endWord:
                return time
            
            for nei in word_map[node]:
                if nei not in visited:
                    queue.append([nei, time +1])
                    visited.add(nei)

        return 0



        

            
        
