class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        if (len(s) == 1):
            return s
        
        for i in range(len(s)//2):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
            
        return s
            
            
        