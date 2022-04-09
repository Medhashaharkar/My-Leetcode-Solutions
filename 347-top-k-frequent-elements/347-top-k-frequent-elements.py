class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_freq = {}
        
        for n in nums:
            if (n in num_freq.keys()):
                num_freq[n] = num_freq[n]+1
            else:
                num_freq[n] = 1
                
        num_freq = dict(sorted(num_freq.items(), key=lambda item: item[1])) 
        
        print(num_freq)
        
        return list(num_freq.keys())[-k:]
            