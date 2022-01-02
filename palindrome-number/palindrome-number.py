class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        s = list(str(x))
        i = 0
        j = len(s)-1-i
        while (i <= int(len(s)/2)):
            if (s[i] != s[j]):
                return False
            else:
                i = i+1
                j = j-1
        return True
            
        