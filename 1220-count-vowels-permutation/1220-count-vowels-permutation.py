import re

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        '''
        def validate_permutations(p):
        
            indices = [i.start() for i in re.finditer("a", p)]
            for i in indices:
                if (i != len(p)-1 and p[i+1]!= "e"):
                    return False

            indices = [i.start() for i in re.finditer("e", p)]
            for i in indices:
                if (i != len(p)-1 and not (p[i+1]== "a" or p[i+1]== "i")):
                    return False

            indices = [i.start() for i in re.finditer("i", p)]
            for i in indices:
                if (i != len(p)-1 and p[i+1]== "i"):
                    return False

            indices = [i.start() for i in re.finditer("o", p)]
            for i in indices:
                if (i != len(p)-1 and not (p[i+1]== "i" or p[i+1]=="u")):
                    return False

            indices = [i.start() for i in re.finditer("u", p)]
            for i in indices:
                if (i != len(p)-1 and p[i+1]!= "a"):
                    return False

            return True
                
        
        def make_permutations(prev_perm):
            perm_1 = ["a", "e", "i", "o", "u"]
            perm = []
            
            for pp in prev_perm:
                for p in perm_1:
                    if (validate_permutations(pp+p)):
                        perm.append(pp+p)
            
            return perm
        
        dp = [0]*(n+1)
        dp[0] = [""]
        
        for i in range(1, n+1):
            dp[i] = make_permutations(dp[i-1])
        print(dp[n])    
        return len(dp[n])
        '''
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n - 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
        return (a + e + i + o + u) % (10**9 + 7)