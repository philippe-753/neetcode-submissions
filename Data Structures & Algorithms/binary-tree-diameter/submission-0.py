# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max_dia = 0

        def dfs(node):

            if not node:
                return 0
            
            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)

            self.max_dia = max(self.max_dia, left+right -2)

            return max(left, right)
        
        dfs(root)
        return self.max_dia
