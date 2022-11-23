# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    result = True
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None :
            return True
        
       
        def RF(node):
            
            if node is None:
                return 0

            left = RF(node.left)
            
            right = RF(node.right)

            if abs(left-right)>=2:
                self.result = False

            return max(left,right)+1

        RF(root)
        return self.result