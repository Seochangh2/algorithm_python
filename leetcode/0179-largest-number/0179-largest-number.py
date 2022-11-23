class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def judge(n1,n2):
            return str(n1)+str(n2) < str(n2)+str(n1)
        idx = 1
        while idx < len(nums):
            j = idx

            while j>0 and judge(nums[j-1],nums[j]):
                nums[j-1] , nums[j] = nums[j],nums[j-1]
                j-=1

            idx += 1

        return str(int(''.join(map(str,nums))))