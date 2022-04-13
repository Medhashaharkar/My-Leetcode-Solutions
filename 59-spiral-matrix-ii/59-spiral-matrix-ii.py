class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        if (n ==1):
            return [[1]]
        
        matrix = []
        
        for r in range(n):
            matrix.append([0]*n)
            
        r0, c0 = 0, 0
        r1, c1 = n-1, n-1
        val = 0
        
        while (r0<r1 and c0<c1):
            
            for i in range(c0, c1+1):
                val += 1
                matrix[r0][i] = val
            
            for i in range(r0+1, r1+1):
                val += 1
                matrix[i][c1] = val
                
            for i in range(c1-1, c0-1, -1):
                val += 1
                matrix[r1][i] = val
                
                
            for i in range(r1-1, r0, -1):
                val += 1
                matrix[i][c0] = val
                
            r0 += 1
            c0 += 1
            r1 -= 1
            c1 -= 1
            
            if (n%2 != 0):
                matrix[n//2][n//2] = n*n
        
        return matrix
            