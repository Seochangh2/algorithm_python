class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.head , self.tail = ListNode(None),ListNode(None)
        self.k , self.len = k,0
        self.head.right,self.tail.left = self.tail , self.head
        
    def _add(self,node, newNode):
        tmpNode = node.right
        node.right = newNode
        newNode.left ,newNode.right , tmpNode.left = node,tmpNode,newNode
        
    def _remove(self,node):
        tmpNode = node.right.right
        node.right ,tmpNode.left= tmpNode,node
        
    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.len >= self.k :
            return False
        self.len += 1
        self._add(self.head,ListNode(value))
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.len >= self.k :
            return False
        self.len += 1
        tmp = self.tail.left 
        self._add( tmp , ListNode(value) )
        return True
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.len == 0 :
            return False
        self.len -= 1
        self._remove(self.head)
        return True
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.len == 0 :
            return False
        self.len -= 1
        self._remove(self.tail.left.left)
        return True
        

    def getFront(self):
        """
        :rtype: int
        """
        if self.len == 0 :
            return -1
        return self.head.right.val
        

    def getRear(self):
        """
        :rtype: int
        """
        if self.len == 0 :
            return -1
        return self.tail.left.val
    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.len == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.len == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()