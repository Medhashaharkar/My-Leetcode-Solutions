class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        s = list(s)
        diff_count = 0
        i = 0
        j = len(s)-1-i
        
        while (i<len(s)//2 and diff_count < 2):
            if (s[i] == s[j]):
                i = i+1
                j = j-1
            else:
                diff_count += 1
                if (s[i+1] == s[j]):
                    i = i+1
                elif (s[j-1] == s[i]):
                    j = j-1
                else:
                    result1 = False
        
        if (diff_count < 2):
            result1 = True
        else:
            result1 = False
            
        diff_count = 0
        i = 0
        j = len(s)-1-i
        
        while (i<len(s)//2 and diff_count < 2):
            if (s[i] == s[j]):
                i = i+1
                j = j-1
            else:
                diff_count += 1
                if (s[j-1] == s[i]):
                    j = j-1
                elif (s[i+1] == s[j]):
                    i = i+1
                else:
                    result2 = False
        
        if (diff_count < 2):
            result2 = True
        else:
            result2 = False
            
        if (result1 == True or result2 == True):
            return True
        else:
            return False