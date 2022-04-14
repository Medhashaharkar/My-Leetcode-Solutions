# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        ptr = root
        while (ptr != None and ptr.val != val):
            if (val < ptr.val):
                ptr = ptr.left
            else:
                ptr = ptr.right
                
        if ptr:
            return ptr
        else:
            return None
            
            
            
                
        