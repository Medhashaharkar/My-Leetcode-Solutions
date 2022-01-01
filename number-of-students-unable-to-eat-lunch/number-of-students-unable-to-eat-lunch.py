class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        #sandwich -> stack
        #student -> queue
        
        
        while len(sandwiches) >= 1 and sandwiches[0] in students:
            
            if (sandwiches[0] == students[0]):
                sandwiches.pop(0)
                students.pop(0)
            else:
                students.append(students.pop(0))
                
        return len(students)
                
                
                
        