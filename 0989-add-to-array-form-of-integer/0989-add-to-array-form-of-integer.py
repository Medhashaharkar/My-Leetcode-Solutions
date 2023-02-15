class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        
        
        num = [str(i) for i in num]
        num = "".join(num)
        print(num)
        num = int(num)
        num = num+k
        num = str(num)
        num = list(num)
        num = [int(i) for i in num]
        
        return num