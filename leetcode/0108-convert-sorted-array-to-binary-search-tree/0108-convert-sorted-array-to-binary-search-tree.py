# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        length = len(nums)
        mid = length/2
        tree = TreeNode(nums[mid])
        tree.left = self.sortedArrayToBST(nums[0:mid])
        tree.right = self.sortedArrayToBST(nums[mid+1:])
        
        return tree