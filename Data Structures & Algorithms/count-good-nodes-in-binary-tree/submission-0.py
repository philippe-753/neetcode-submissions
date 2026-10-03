# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.res = 0

        def dfs(node, prev_node):

            if not node:
                return 0
            if node.val >= prev_node:
                self.res += 1
                dfs(node.left, node.val)
                dfs(node.right, node.val)
            else:
                dfs(node.left, prev_node)
                dfs(node.right, prev_node)

        dfs(root, -float("inf"))
        return self.res

            