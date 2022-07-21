class MyQueue(object):

    def __init__(self):
        self.input = []
        self.output=[]
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.input.append(x)
        self.output = list(reversed(self.input))
    def pop(self):
        """
        :rtype: int
        """
        pop = self.output.pop()
        self.input = list(reversed(self.output))
        return pop

    def peek(self):
        """
        :rtype: int
        """
        return self.output[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.input)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()