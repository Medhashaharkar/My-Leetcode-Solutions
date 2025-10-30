class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        i = 0
        j = 0
        while i<len(t) and j<len(s):
            if (t[i] == s[j]):
                j+=1
            i += 1

        if j == len(s):
            return True
        else:
            return False

        
        