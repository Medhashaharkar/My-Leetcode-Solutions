class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        result = {}

        def findPath(row, col):
            if row == 0 or col == 0:
                return 1
            elif (row, col) not in result:
                result[(row, col)] = findPath(row-1, col) + findPath(row, col-1)
            return result[(row, col)]
        
        return findPath(m-1, n-1)


        
        