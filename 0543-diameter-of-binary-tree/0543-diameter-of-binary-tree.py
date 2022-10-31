# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    result=0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
            
        def findDepth(tree):
            if tree is None:
                return -1

            left = findDepth(tree.left)
            right = findDepth(tree.right)
            self.result = max(self.result,left+right+2)
                    
            return max(left,right)+1
        
        findDepth(root)
        
        return self.result
            
        
        