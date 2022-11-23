class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def dfs(target,nums):
            if target == 0 :
                nums.sort(reverse=True)
                if nums not in result:
                    result.append(nums[:])
                return
            elif target < 0:
                return
                
            for can in candidates:
                dfs(target-can,nums+[can])

            

        dfs(target,[])
        return result
    
        