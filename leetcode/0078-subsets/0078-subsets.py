class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]

        
        def dfs(count,mynums):
            result.append(mynums)
            for i in range(count,len(nums)):
                dfs(i+1,mynums+[nums[i]])
                
        dfs(0,[])
        return result