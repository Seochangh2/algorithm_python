class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start < end:
            idx = start + (end-start)//2
            if nums[idx]>nums[end]:
                start = idx+1
            else :
                end = idx

        t_index = start

        start , end = 0,len(nums)-1

        while start<=end:
            idx = start + (end-start)//2
            t_idx = (idx+t_index)%len(nums)

            if target > nums[t_idx]:
                start = idx+1
            elif target < nums[t_idx]:
                end = idx-1
            else :
                return t_idx
        return -1 

