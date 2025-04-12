class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])

        def bsearch(left, right):
            if left>right:
                return False
            
            mid = (left+right)//2
            row = mid // n
            col = mid % n

            if target==matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                return bsearch(mid+1, right)
            else:
                return bsearch(left, mid-1)
        
        return bsearch(0, m * n - 1)
        