# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        visited = []
        
        ptr = head
        
        while ptr.next!=None:
            if (ptr not in visited):
                visited.append(ptr)
                ptr = ptr.next
            if (ptr in visited):
                return ptr
        
        return None
                
        