class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        tmp = 1
        for i in range(len(nums)):
            output.append(tmp)
            tmp *= nums[i]
        
        tmp = 1
        
        for i in range(len(nums)):
            output[len(nums)-1-i] = output[len(nums)-1-i]*tmp
            tmp *= nums[len(nums)-1-i]
            
        return output