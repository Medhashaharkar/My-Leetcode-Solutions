class Solution:
    def mySqrt(self, x: int) -> int:

        for i in range(0, (x//2)+2):
            if (i*i == x):
                return i
            elif (i*i > x):
                return i-1
        
        