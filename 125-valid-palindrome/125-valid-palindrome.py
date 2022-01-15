import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        result = re.sub(r'[^a-zA-Z0-9]', '', s)
        result = result.lower()
        
        print(result)
        
        if not result:
            return True
        
        for i in range(int(len(result)/2)):
            j = len(result)-1-i
            if (result[i] != result[j]):
                return False
        return True
        
        