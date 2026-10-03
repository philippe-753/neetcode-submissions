"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        
        graph_clone = {}
        
        def dfs(node):

            if node in graph_clone:
                return graph_clone[node]
            
            clone = Node(node.val)
            graph_clone[node] = clone

            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
        
            return clone
        
        return dfs(root) if root else None


            