class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        result = [1,2,3,4,5,6,7,8,9]
        
        for _ in range(n-1):
            cur = result
            result = []
            for c in cur:
                rem = c%10
                if (rem+k < 10):
                    result.append(c*10+rem+k)
                if (rem-k >= 0):
                    result.append(c*10+rem-k)
        
        return set(result)
            
            