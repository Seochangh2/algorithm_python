class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        end = len(nums)-1
        start = 0
        while start <= end :
            idx = (end+start)//2
            if target > nums[idx] :
                start=idx+1
            elif target < nums[idx] :
                end = idx-1
            else :
                return idx
        
        return -1