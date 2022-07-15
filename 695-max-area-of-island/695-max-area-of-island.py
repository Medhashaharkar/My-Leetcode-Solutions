class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def calcArea(i, j, m, n, grid):
            
            if (i<0 or j<0 or i>=m or j>=n):
                return 0
            elif (grid[i][j] == 0):
                return 0
            elif (grid[i][j] == 1):
                grid[i][j] = 0
                area = 1
                area += calcArea(i+1, j, m, n, grid)
                area += calcArea(i-1, j, m, n, grid)
                area += calcArea(i, j+1, m, n, grid)
                area += calcArea(i, j-1, m, n, grid)
                
                return area
         
        max_area = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = calcArea(i, j, len(grid), len(grid[0]), grid)
                if (area > max_area):
                    max_area = area
        return max_area
                
        