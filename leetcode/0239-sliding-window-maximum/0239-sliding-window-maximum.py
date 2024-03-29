class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = collections.deque()
        c_max = float('-inf')
        result = []
        for i in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)
            if dq[0] == i-k:
                dq.popleft()
            if i >= k-1:
                result.append(nums[dq[0]])
        return result
            