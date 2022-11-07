class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        
        
        # for num in nums:
        #     if num not in heap:
        #         heapq.heappush(heap,num)
        heapq.heapify(nums)
        result = 0
        for _ in range(0,len(nums)-k):
            result = heapq.heappop(nums)
        return nums[0]