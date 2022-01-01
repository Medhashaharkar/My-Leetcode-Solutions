class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        if (s[0] not in s[1:]):
            return 0
        
        for i in range(1, len(s)-1):
            if (s[i] not in s[i+1:] and s[i] not in s[:i]):
                return i
            
        if (s[len(s)-1] not in s[:len(s)-1]):
            return len(s)-1
            
        return -1
        