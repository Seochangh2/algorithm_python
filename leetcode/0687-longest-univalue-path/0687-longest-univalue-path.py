# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    result = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(tree):
            if tree is None:
                return 0
            left = dfs(tree.left)
            right = dfs(tree.right)

            if tree.left and tree.left.val == tree.val:
                left += 1
            else:
                left = 0
            if tree.right and tree.right.val == tree.val:
                right +=1
            else:
                right = 0
            
            self.result = max(self.result,left+right)
            return max(left,right)
        dfs(root)
        return self.result