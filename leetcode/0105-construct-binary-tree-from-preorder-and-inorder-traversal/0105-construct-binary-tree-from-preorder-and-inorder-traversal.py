# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            val = preorder.pop(0)
            idx = inorder.index(val)

            root = TreeNode(val)
            root.left = self.buildTree(preorder ,inorder[0:idx])
            root.right = self.buildTree(preorder,inorder[idx+1:])

            return root