class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        a,b = 0 , len(matrix[0])-1
        while a < len(matrix) and b>=0:
            if matrix[a][b] < target:
                a+=1
            elif matrix[a][b] > target:
                b-=1
            else:
                return True