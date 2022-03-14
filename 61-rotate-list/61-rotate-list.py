# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None:
            return head
        
        ptr1=head
        l = 0
        nums = []
        
        while (ptr1!=None):
            l += 1
            nums.append(ptr1.val)
            ptr1= ptr1.next
        
        i=0
            
        ptr1 = head
        
        while(ptr1!=None):
            ptr1.val = nums[(i-k)%l]
            ptr1 = ptr1.next
            i = (i+1)%l
            
        return head
            
            
        