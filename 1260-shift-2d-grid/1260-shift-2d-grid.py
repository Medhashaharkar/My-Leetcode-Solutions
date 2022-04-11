class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        for _ in range(k):
        
            last_col = [0]*len(grid)

            for i in range(len(grid)):
                last_col[(i+1)%len(grid)] = grid[i][len(grid[0])-1]

            for i in range(len(grid)):
                for j in range(len(grid[0])-1,0,-1):
                    grid[i][j] = grid[i][j-1]

            for i in range(len(grid)):
                grid[i][0] = last_col[i]
                
        return grid
            
            
                
        