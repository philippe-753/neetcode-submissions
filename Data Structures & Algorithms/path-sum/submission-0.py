# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, cur):
            if not node: return False
            if not node.left and not node.right and cur + node.val == targetSum: return True
            if node.left and dfs(node.left, cur + node.val): return True
            if node.right and dfs(node.right, cur + node.val): return True
            return False
        return dfs(root, 0)