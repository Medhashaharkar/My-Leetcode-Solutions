class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if (not s and not t):
            return True
        
        if (len(s) > len(t)):
            return False
        
        if (len(s) == len(t)):
            if (s == t):
                return True
            else:
                return False
            
        for i in range(len(s)):
            if (s[i] in t):
                t = t[t.index(s[i])+1:]
            else:
                return False
        return True
            
            
        