class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums2 or not nums1:
            return
        result = []
        nums2.sort()
        for n1 in nums1:
            idx2 = bisect.bisect_left(nums2,n1)
            if len(nums2)>idx2 and nums2[idx2] == n1 and n1 not in result:
                result.append(n1)
                
        return result