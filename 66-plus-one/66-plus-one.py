class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            summed = digits[i] + carry
            
            if summed>9:
                carry = int(str(summed)[0])
                summed = int(str(summed)[1])
            else:
                carry = 0
                
            digits[i] = summed
        
        if (carry > 0):
            digits.insert(0,carry)
            
        return digits
            
                
            
        