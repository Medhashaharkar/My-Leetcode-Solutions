class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        tri = []
        tri.append([1])
        tri.append([1,1])
        
        for i in range (2, rowIndex+1):
            tri.append([1])
            
            for j in range(len(tri[i-1])-1):
                tri[i].append(tri[i-1][j]+tri[i-1][j+1])
            
            tri[i].append(1)
            
        return tri[rowIndex]
            
            
        