# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    result =100000000 
    pre = -1000000
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left :
            self.minDiffInBST(root.left)
            
        self.result = min(self.result,root.val - self.pre)
        self.pre = root.val
        if root.right :
            self.minDiffInBST(root.right)
        
        return self.result
        