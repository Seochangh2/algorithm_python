class Solution(object):
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        if L == 1:
            return nums[0]
        if L == 2:
            return max(nums)
        memory = collections.OrderedDict()

        memory[0] = nums[0]
        memory[1] = max(nums[1],nums[0])
        for i in range(2,L):
            memory[i] = max(memory[i-1],memory[i-2]+ nums[i])
        return memory[L-1]