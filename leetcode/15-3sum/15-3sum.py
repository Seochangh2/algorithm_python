class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output =[]
        if(len(nums)<3):
            return output
        nums.sort()
        
        def findSum(index) :
            first = index+1
            second = len(nums)-1
            while( first < second ):
                if nums[index] + nums[first] +nums[second] ==0 :
                    if [ nums[index] , nums[first] ,nums[second]] not in output:
                        output.append([ nums[index] , nums[first] ,nums[second]])
                    first +=1
                elif nums[index] + nums[first] +nums[second] < 0 :
                    first +=1
                elif nums[index] + nums[first] +nums[second] > 0 :
                    second -=1
                    
        for i in range(0,len(nums)-2):
            findSum(i)
            
        return output
            