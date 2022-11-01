# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque([root])
        result = []
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else :
                result.append("#")

        return ' '.join(result)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nums = data.split()
        if nums[0]=='#':
            return

        root = TreeNode(int(nums[0]))
        index = 1
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                if nums[index] != '#':
                    node.left = TreeNode(int(nums[index]))
                    queue.append(node.left)
                else : 
                    node.left = None
                index += 1
                if nums[index] != '#':
                    node.right = TreeNode(int(nums[index]))
                    queue.append(node.right)
                else : 
                    node.right = None
                index += 1
        return root
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))