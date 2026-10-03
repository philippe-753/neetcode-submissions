# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None

        val = preorder[0]
        node = TreeNode(val)
        idx = inorder.index(val)

        node.left = self.buildTree(
            preorder = preorder[1:idx+1],
            inorder = inorder[:idx]
        )
        node.right = self.buildTree(
            preorder = preorder[idx+1:],
            inorder = inorder[idx+1:]
        )

        return node





"""

preorder =  [1, 2, 4, 5, 3, 6]
inoder = [4, 5, 2, 1, 3, 6]


"""