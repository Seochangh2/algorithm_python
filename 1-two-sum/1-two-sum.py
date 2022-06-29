class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if (target-nums[i]) in nums:
                if nums.index((target-nums[i])) != i:
                    valid = nums.index((target-nums[i]))
                    return [i,valid]