class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        refer = dict(zip(string.ascii_uppercase, range(1,27)))
        
        col = columnTitle[::-1]
        
        result = 0
        
        for i in range(len(col)):
            result = result + refer[col[i]]*pow(26,i)
            
        return result
            
        
            