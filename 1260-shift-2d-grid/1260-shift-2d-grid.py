class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m = len(grid)
        n = len(grid[0])
        
        for _ in range(k):
        
            last_col = [0]*m

            for i in range(m):
                last_col[(i+1)%m] = grid[i][n-1]

            for i in range(m):
                for j in range(n-1,0,-1):
                    grid[i][j] = grid[i][j-1]

            for i in range(m):
                grid[i][0] = last_col[i]
                
        return grid
            
            
                
        