class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums)

        output = [ e[0] for e in counter.most_common(k)]
            
        
        
        return output
            