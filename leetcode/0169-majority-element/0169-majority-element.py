class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leng = len(nums)
        counter = collections.defaultdict(int)

        def devide(array):
            if len(array)==1:
                return array[0]
            mid = len(array)//2

            L = devide(array[:mid])
            
            R = devide(array[mid:])
            
            counter[L]+=1
            counter[R]+=1

            return [L,R][array.count(R)>mid]
            
        result = devide(nums)
        
        return result