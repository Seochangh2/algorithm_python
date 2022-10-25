class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        numbers = list(range(1,n+1))
        result = list(itertools.combinations(numbers,k))

        return result