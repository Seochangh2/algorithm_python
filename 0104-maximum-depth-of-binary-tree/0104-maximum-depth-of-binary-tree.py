# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None :
            return 0
        queue = collections.deque([root])
        depth = 0 

        while queue:
            depth += 1

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
        return depth