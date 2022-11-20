class Solution(object):
    memory = collections.defaultdict(int)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        if self.memory[n]:
            return self.memory[n]
        
        self.memory[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memory[n]