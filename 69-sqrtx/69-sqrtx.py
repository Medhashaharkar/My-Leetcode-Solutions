class Solution:
    def mySqrt(self, x: int) -> int:
        
        s = 0
        
        while s*s <= x :
            s = s+1
            
        return s-1
            
        