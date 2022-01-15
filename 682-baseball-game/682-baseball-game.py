class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        result = []
        
        for i in range(len(ops)):
            if (ops[i] == "D"):
                result.append(int(result[-1])*2)
            elif (ops[i] == "C"):
                result.pop()
            elif (ops[i] == "+"):
                result.append(int(result[-1])+int(result[-2]))
            else:
                result.append(int(ops[i]))
                
        return sum(result)
        