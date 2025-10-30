class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        i = 0
        j = 0
        for i in range(len(t)):
            if j>len(s)-1:
                break
            print("i", i)
            print("j", j)
            if (t[i] == s[j]):
                j+=1

        if j == len(s):
            return True
        else:
            return False

        
        