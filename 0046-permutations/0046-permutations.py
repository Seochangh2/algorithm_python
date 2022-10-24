class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def dfs(output,numbers):
            if len(output) == len(nums):
                result.append(output[:])
                return
                
            for number in numbers:
                output.append(number)
                tmpnumbers = numbers[:]
                tmpnumbers.remove(number)
                dfs(output,tmpnumbers)
                output.pop()

        dfs([],nums)
        return result