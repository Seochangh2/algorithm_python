class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        c_max = float('-inf')
        queue = collections.deque()

        for i,v in enumerate(nums):
            while queue and nums[queue[-1]] <= v:
                queue.pop()
            queue.append(i)
            
            if queue[0] == i-k:
                queue.popleft()
            
            if i >= k-1:
                result.append(nums[queue[0]])
        return result