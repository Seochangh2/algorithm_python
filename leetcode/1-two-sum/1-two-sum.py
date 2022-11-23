class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dic = {}
        for i,num in enumerate(nums):
            num_dic[num] = i
            
        for i,num in enumerate(nums):
            if (target-num) in num_dic and i != num_dic[target-num]:
                return[i,num_dic[target-num]]