class Solution:
    def minDeletions(self, string: str) -> int:
        
        '''
        def delete_chars(arr):
            dup = [x for x in arr if arr.count(x) > 1]
            
            for i in arr:
                if i in dup:
                    i = i-1
                    return arr
                
        freq = {}
        
        for s in string:
            if s in freq.keys():
                freq[s] = freq[s]+1
            else:
                freq[s] = 1
        
        arr = list(freq.values())
        count = 0
        while (len(set(arr)) != len(arr)):
            count = count+1
            arr = delete_chars(arr)
               
        return count
        
        '''

        freq = collections.Counter(string)
        count = 0
        used_freq = set()

        for s,f in freq.items():
            while f > 0 and f in used_freq:
                f = f-1
                count = count+1
            used_freq.add(f)

        return count
            
            
            
        
            
            
        