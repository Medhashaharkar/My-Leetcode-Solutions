class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        while n>0:
            if (n == 1):
                return True
            else:
                n = n/3
        
        return False
        