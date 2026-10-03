from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        queue = deque([["0000", 0]])
        visited = set()

        while queue:
            node, count = queue.popleft()

            if node in deadends or node in visited:
                continue

            visited.add(node)
            if node == target:
                return count

            for i in range(4):
                inter = int(node[i:i+1])
                inter_add, inter_sub = inter + 1, inter - 1
                if inter_add >= 10:
                    inter_add = 0
                if inter_sub <= -1:
                    inter_sub = 9
                
                node_add, node_sub = node[:i] + str(inter_add) + node[i+1:], node[:i] + str(inter_sub) + node[i+1:] 
                queue.append([node_add, count+1])
                queue.append([node_sub, count+1])
        
        return -1 


        