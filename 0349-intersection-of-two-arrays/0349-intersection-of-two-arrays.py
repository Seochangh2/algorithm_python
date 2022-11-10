class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        
        if len(nums1) >= len(nums2):
            for n2 in nums2:
                if n2 in nums1:
                    if n2 not in result:
                        result.append(n2)
        else:
            for n1 in nums1:
                if n1 in nums2:
                    if n1 not in result:
                        result.append(n1)
        return result
                