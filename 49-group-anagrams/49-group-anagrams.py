class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}
        
        for i in strs:
            sorted_i = "".join(sorted(list(i)))
            if (sorted_i in anagrams.keys()):
                anagrams[sorted_i].append(i)
            else:
                anagrams[sorted_i] = [i]
                
        return anagrams.values()
                
                
        