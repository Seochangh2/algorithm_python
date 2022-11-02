# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    val = 0
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def RF(node):
            if not node :
                return 
            RF(node.right)
            node.val += self.val
            self.val = node.val
            RF(node.left)

        
        RF(root)
        return root
                    