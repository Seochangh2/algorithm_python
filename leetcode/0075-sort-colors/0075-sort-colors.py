class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        white , red , blue = 0 , 0 , len(nums)
        
        while red < blue:
            if nums[red] < 1:
                nums[white] , nums[red] = nums[red] , nums[white]
                white +=1
                red += 1
            elif nums[red] > 1:
                blue -=1
                nums[blue] , nums[red] = nums[red] , nums[blue]
            else :
                red += 1